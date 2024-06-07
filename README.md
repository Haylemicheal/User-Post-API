User API
========

This project is a User API built using FastAPI, SQLAlchemy, and Docker. It includes authentication, posting, and caching functionality with a MySQL database and Redis for caching.

Project Structure
-----------------

blog\_api/
├── app/
│   ├── \_\_init\_\_.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── routes/
│   │   ├── \_\_init\_\_.py
│   │   ├── auth.py
│   │   ├── post.py
│   └── utils/
│       ├── \_\_init\_\_.py
│       ├── auth.py
│       ├── cache.py
│       ├── dependencies.py
├── docker-compose.yml
├── requirements.txt
└── .env

Setup and Installation
----------------------

### Prerequisites

* Docker and Docker Compose
* Python 3.8+

### Steps

1. **Clone the repository:**

   git clone <repository-url>
   cd blog\_api
2. **Create the Docker Compose file and project structure:**

   ./setup\_project.sh
3. **Start the Docker containers:**

   docker-compose up -d
4. **Install Python dependencies:**

   pip install -r requirements.txt
5. **Set up environment variables:**

   The `.env` file should be created automatically by the setup script. If not, create it with the following content:

   \# .env file

   # Database configuration

   DATABASE\_URL=mysql+mysqlclient://root:my-secret-pw@mysql-container/mydatabase

   # JWT secret key

   SECRET\_KEY=your\_secret\_key

   # JWT algorithm

   ALGORITHM=HS256

   # Access token expiration time (in minutes)

   ACCESS\_TOKEN\_EXPIRE\_MINUTES=30

   # Redis configuration

   REDIS\_HOST=redis-container
   REDIS\_PORT=6379
   REDIS\_DB=0
6. **Run database migrations:**

   To be added: details on running Alembic migrations (if you decide to use Alembic for managing database migrations).
7. **Run the FastAPI application:**

   uvicorn app.main:app --reload
8. **Access the application:**

   Open your browser and go to `http://localhost:8000` to access the API. The automatically generated API documentation will be available at `http://localhost:8000/docs`.

API Endpoints
-------------

### Signup

* **Endpoint:** `/signup`
* **Method:** `POST`
* **Request Body:**

  {
  "email": "user@example.com",
  "password": "password123"
  }
* **Response:** Returns a token (JWT or randomly generated string).

### Login

* **Endpoint:** `/login`
* **Method:** `POST`
* **Request Body:**

  {
  "email": "user@example.com",
  "password": "password123"
  }
* **Response:** Returns a token upon successful login; error response if login fails.
