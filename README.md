User API
========

This project is a User POST API built using FastAPI, SQLAlchemy, and Docker. It includes authentication, posting, and caching functionality with a MySQL database and Redis for caching.

### Project Structure Explanation

- **app/**: This directory contains the main code for the FastAPI application.
  - **main.py**: Entry point of the FastAPI application.
  - **models.py**: Contains SQLAlchemy models for database tables.
  - **schemas.py**: Defines Pydantic models for data validation.
  - **database.py**: Configures the database connection.
  - **crud.py**: Contains CRUD operations for interacting with the database.
  - **routes/**: Contains API endpoints for different functionalities.
    - **auth.py**: Implements authentication-related endpoints.
    - **post.py**: Implements endpoints related to posts.
  - **utils/**: Contains utility functions and dependencies.
    - **auth.py**: Implements authentication utilities.
    - **cache.py**: Handles caching functionality.
    - **dependencies.py**: Defines dependency injections.

- **docker-compose.yml**: Docker Compose file for setting up Docker containers.
- **requirements.txt**: List of Python dependencies required by the project.
- **.env**: Environment variable file for configuring database and other settings.




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
