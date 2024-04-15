
# Backend Challenge Task Manager API Project Setup Guide

This document provides a comprehensive guide on how to set up and run the Task Manager API locally. The project is built using Django and Django Rest Framework, designed to manage tasks and labels with user authentication.

## Prerequisites

Before beginning, ensure you have the following installed on your system:
- Python 3.8 or higher
- Django 3.1 or higher
- Django Rest Framework

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Cloning the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/backend-challenge.git
cd backend-challenge
```

Replace `https://github.com/yourusername/backend-challenge.git` with the actual URL of your repository.

### Setting Up the Virtual Environment

Create and activate a virtual environment:

#### For Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### For macOS and Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Installing Dependencies

Install all the required packages:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file does not exist, install Django and DRF directly:

```bash
pip install django djangorestframework
```

### Database Setup

Run migrations to set up your database:

```bash
python manage.py migrate
```

### Creating Superuser

Create an administrative user for accessing the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the username, email, and password.

### Running the Development Server

Start the local development server:

```bash
python manage.py runserver
```

The server will start, typically accessible via `http://127.0.0.1:8000`.

## Testing the Application

To test if your application is running correctly:

1. Open a web browser and go to `http://127.0.0.1:8000/admin` to access the admin interface.
2. Log in with the superuser credentials you created earlier.
3. Verify that you can access the admin dashboard and see the Task and Label models.

## API Endpoints

You can access the following API endpoints:

- **Tasks**: `http://127.0.0.1:8000/api/tasks/`
- **Labels**: `http://127.0.0.1:8000/api/labels/`
- **Token Authentication**: `http://127.0.0.1:8000/api-token-auth/`

Use tools like Postman to test API requests.

## User Credentials
The following credentials are available for testing:

- **Username**: `username1`
- **Password**: `password1`

