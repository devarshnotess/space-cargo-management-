import datetime
from sqlalchemy.orm import Session
import crud, schemas

def recommend_placement(item: schemas.ItemCreate, db: Session):
    """
    Advanced placement recommendation:
    - Evaluate all containers in the item's preferred zone.
    - Calculate free volume and choose the container with the minimal leftover free volume that can fit the item.
    - Assign a simple coordinate based on the number of items already present.
    """
    containers = crud.get_containers(db)
    item_volume = item.width * item.depth * item.height
    candidate = None
    min_leftover = None
    chosen_pos = None
    for container in containers:
        if container.zone == item.preferred_zone:
            container_volume = container.width * container.depth * container.height
            used_volume = sum(i.width * i.depth * i.height for i in container.items)
            free_volume = container_volume - used_volume
            if free_volume >= item_volume:
                leftover = free_volume - item_volume
                if min_leftover is None or leftover < min_leftover:
                    min_leftover = leftover
                    candidate = container
                    # For a robust placement, if container is empty, use origin; otherwise, assign based on count.
                    count = len(container.items)
                    chosen_pos = {
                        "pos_width": (count * item.width) % container.width,
                        "pos_depth": (count * item.depth) % container.depth,
                        "pos_height": (count * item.height) % container.height
                    }
    return candidate, chosen_pos

def calculate_retrieval_steps(item_id: str, db: Session):
    """
    Calculate the number of steps required to retrieve the item.
    Steps are defined as the number of items that must be moved (i.e. are placed before the target item) in the container.
    """
    db_item = crud.get_item_by_item_id(db, item_id)
    if not db_item or not db_item.container:
        return None
    # Sort items in the container by their position coordinates
    items = sorted(db_item.container.items, key=lambda x: (x.pos_width, x.pos_depth, x.pos_height))
    steps = 0
    for i in items:
        if i.id == db_item.id:
            break
        steps += 1
    return steps

def simulate_days(db: Session, num_days: int):
    """
    Simulate the passage of time by advancing the simulation date.
    - Update the current simulation date.
    - Mark items as 'waste' if their expiry_date is before the new simulation date.
    """
    sim = crud.get_simulation(db)
    if not sim:
        sim = crud.create_simulation(db)
    new_date = sim.current_date + datetime.timedelta(days=num_days)
    sim.current_date = new_date
    db.commit()
    db.refresh(sim)
    # Update status for each active item if expired or usage limit reached.
    items = crud.get_items(db)
    for item in items:
        if item.status == "active" and item.expiry_date < new_date:
            item.status = "waste"
    db.commit()
    return sim
  
