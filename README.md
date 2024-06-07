User Post API
=============

This project is a User Post API built using FastAPI, SQLAlchemy, and Docker. It includes user authentication, posting functionality, and caching with a MySQL database and Redis for caching.

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
   cd blog_api

   2. **Create the Docker Compose file and project structure:**

      Run the setup script to create the necessary files and directory structure.

      ./setup_project.sh

      3. **Start the Docker containers:**

         docker-compose up -d

         4. **Install Python dependencies:**

            pip install -r requirements.txt

            5. **Set up environment variables:**

               The `.env` file should be created automatically by the setup script. If not, create it with the following content:

               # .env file

               # Database configuration
               DATABASE_URL=mysql+mysqlclient://root:my-secret-pw@mysql-container/mydatabase

               # JWT secret key
               SECRET_KEY=your_secret_key

               # JWT algorithm
               ALGORITHM=HS256

               # Access token expiration time (in minutes)
               ACCESS_TOKEN_EXPIRE_MINUTES=30

               # Redis configuration
               REDIS_HOST=redis-container
               REDIS_PORT=6379
               REDIS_DB=0

               6. **Run database migrations:**

                  To be added: details on running Alembic migrations (if you decide to use Alembic for managing database migrations).
               7. **Run the FastAPI application:**

                  uvicorn app.main:app --reload

                  8. **Access the application:**

                     Open your browser and go to [http://localhost:8000](http://localhost:8000) to access the API. The automatically generated API documentation will be available at [http://localhost:8000/docs](http://localhost:8000/docs).
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
               ### Login* **Endpoint:** `/login`
               * **Method:** `POST`
               * **Request Body:**

                 {
                     "email": "user@example.com",
                     "password": "password123"
                 }

                 * **Response:** Returns a token upon successful login; error response if login fails.
               ### Add Post* **Endpoint:** `/posts`
               * **Method:** `POST`
               * **Request Headers:**

                 * `Authorization: Bearer <token>`
               * **Request Body:**

                 {
                     "text": "This is a new post"
                 }

                 * **Response:** Returns `postID`.
               ### Get Posts* **Endpoint:** `/posts`
               * **Method:** `GET`
               * **Request Headers:**
                 * `Authorization: Bearer <token>`
               * **Response:** Returns all user's posts. Implements response caching for up to 5 minutes for the same user.


               ### Delete Post

               * **Endpoint:** `/posts/{post_id}`
               * **Method:** `DELETE`
               * **Request Headers:**
                 * `Authorization: Bearer <token>`
               * **Response:** Deletes the corresponding post from memory.
