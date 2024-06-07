#!/bin/bash

# Create the app directory structure
mkdir -p app/routes
mkdir -p app/utils

# Create __init__.py files
touch app/__init__.py
touch app/routes/__init__.py
touch app/utils/__init__.py

# Create the main files
touch app/main.py
touch app/models.py
touch app/schemas.py
touch app/database.py
touch app/crud.py

# Create route files
touch app/routes/auth.py
touch app/routes/post.py

# Create util files
touch app/utils/auth.py
touch app/utils/cache.py
touch app/utils/dependencies.py

# Create requirements.txt
touch requirements.txt

# Print success message
echo "Directory structure and files created successfully!"
