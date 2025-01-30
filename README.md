# FastAPI Project

This is a simple FastAPI project that includes user registration, login, and token-based authentication.

## Requirements

- Python 3.10
- FastAPI
- Uvicorn
- bcrypt
- python-jose
- django-environ

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi_project.git
cd fastapi_project
```

2. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```bash
pip install fastapi uvicorn bcrypt python-jose django-environ
```

4. Set the environment variables:
```bash
export SECRET_KEY="your_secret_key"
export ALGORITHM="HS256"
export ACCESS_TOKEN_EXPIRE_MINUTES=30
```

# Running the Application
## Start the Uvicorn server:

```bash
uvicorn app.main:app --reload
```

The application will be available at http://127.0.0.1:8000.

# API Endpoints
### Register a new user
- URL: /register/
- Method: POST
- Request Body:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
-Response
```json
{
  "msg": "User created successfully!"
}
```

### Login
-URL:/token/
-Method:post
-Request Body:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
-Response
```json
{
  "access_token": "your_access_token",
  "token_type": "bearer",
  "username": "your_username"
}```
### Get all users
-URL:/users
-Method:get
-Response
```json
{
  "username1": {
    "username": "username1",
    "password": "hashed_password"
  },
  "username2": {
    "username": "username2",
    "password": "hashed_password"
  }
}
```
### Get current user
-URL:/users/me
-Method: GET
-Headers:
```json
{
  "Authorization": "Bearer your_access_token"
}
```
-Response
```json
{
  "username": "your_username"
}
```
