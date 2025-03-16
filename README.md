Space Cargo Management System 🚀

An advanced cargo management system for space stations, built with FastAPI (backend) and React.js + Material UI (frontend). This system optimizes cargo storage, retrieval, and simulation.


---

📌 Features

✅ FastAPI Backend with PostgreSQL integration
✅ Advanced Space Optimization (bin-packing logic for item placement)
✅ Time Simulation (simulate cargo expiration over time)
✅ React.js Frontend (Material UI for a modern UI/UX)
✅ Dockerized Deployment


---

📂 Project Structure

space-cargo-management/

├── backend/ 

# FastAPI Backend

│   ├── main.py 

# FastAPI entry point
│   ├── database.py              # PostgreSQL setup
│   ├── models.py                # Database models
│   ├── schemas.py               # API schemas
│   ├── crud.py                  # CRUD operations
│   ├── logic.py                 # Advanced algorithms (storage optimization, retrieval)
│   ├── routes/                   # API Endpoints
│   │   ├── items.py
│   │   ├── containers.py
│   │   ├── simulation.py
│   ├── requirements.txt          # Backend dependencies
│   ├── Dockerfile                # Docker configuration
├── frontend/                     # React.js Frontend
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── Dashboard.js
│   │   │   ├── Items.js
│   │   │   ├── Containers.js
│   │   │   ├── SimulationControl.js
│   ├── package.json              # Frontend dependencies
├── README.md                     # Project documentation


---

🚀 Setup & Installation

1️⃣ Backend (FastAPI + PostgreSQL)

🔹 Prerequisites

Python 3.9+

PostgreSQL installed & running


🔹 Steps

1. Clone the repository:

git clone https://github.com/devarshnotess/space-cargo-management
cd space-cargo-management/backend


2. Create a virtual environment:

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`


3. Install dependencies:

pip install -r requirements.txt


4. Configure your PostgreSQL database (database.py):

DATABASE_URL = "postgresql://user:password@localhost/spacecargo"


5. Initialize the database:

python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"


6. Run the FastAPI server:

uvicorn main:app --reload


7. API Documentation available at:

📌 Swagger UI: http://localhost:8000/docs





---

2️⃣ Frontend (React.js + Material UI)

🔹 Prerequisites

Node.js & npm installed


🔹 Steps

1. Navigate to the frontend directory:

cd ../frontend


2. Install dependencies:

npm install


3. Start the development server:

npm start


4. The frontend will be available at:

🌍 http://localhost:3000





---

🛠 API Endpoints

📦 Items

📦 Containers

⏳ Simulation


---

🐳 Docker Deployment

1️⃣ Build and Run Backend in Docker

cd backend
docker build -t space-cargo-backend .
docker run -p 8000:8000 space-cargo-backend

2️⃣ Build and Run Frontend in Docker

cd ../frontend
docker build -t space-cargo-frontend .
docker run -p 3000:3000 space-cargo-frontend


---

👨‍💻 Contribution Guidelines

1. Fork the repository.


2. Create a new branch (feature/my-feature).


3. Commit your changes (git commit -m "Added new feature").


4. Push to the branch (git push origin feature/my-feature).


5. Create a Pull Request 🚀.




---

🔗 Useful Links

FastAPI Documentation: https://fastapi.tiangolo.com

React.js Documentation: https://react.dev

Material UI: https://mui.com



---

💡 Future Enhancements

✅ Improve item retrieval efficiency
✅ Enhanced simulation features (real-time astronaut interactions)
✅ Deployment to cloud (AWS, GCP, or Heroku)


---

📌 License

This project is licensed under the MIT License.


---

🎯 Summary

🚀 Complete backend with advanced space optimization & simulation

🎨 Beautiful React.js frontend using Material UI

🐳 Dockerized for easy deployment

🔗 Fully documented API


Let me know if you need any modifications to this README! 🚀

