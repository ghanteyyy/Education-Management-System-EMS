# Education Management System (EMS)
An **Education Management System (EMS)** is a centralized digital platform designed to streamline and manage the core operations of educational institutions such as schools, colleges, and training centers. It replaces traditional manual processes with an efficient, scalable, and secure system that connects administrators, teachers, students, and parents in one unified ecosystem.

This EMS focuses on simplifying tasks like student enrollment, academic record management, attendance tracking, scheduling, and communication. By organizing data in a structured way, it enables institutions to make faster decisions, reduce administrative overhead, and improve overall productivity.

## Features

-   JWT Authentication (Access + Refresh Token)
-   Refresh token stored in **HttpOnly Cookies**
-   Django REST Framework (DRF)
-   PostgreSQL support
-   Docker & Docker Compose setup
-   Auto migrations on container start
-   Modular project structure
-   Swagger API Documentation (drf-spectacular)
-   Security best practices (CORS, CSRF, etc.)
-   Ready for production deployment


## Tech Stack

-   Python 3.13
-   Django
-   Django REST Framework
-   PostgreSQL
-   Docker
-   drf-spectacular (Swagger)

## ⚠️ Important: Configure Environment Variables

Before running the project, **make sure to update your `.env` file** with your own configuration.

> ❗ **Do NOT use default or placeholder values in production**

### Example `.env`

```env
DEBUG=False

JWT_SIGNING_KEY=your-jwt-signing-key
DJANGO_SECRET_KEY=your-django-secret-key

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432

ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

## Setup Instructions

### Clone Repository

    git clone https://github.com/ghanteyyy/Education-Management-System-EMS.git
    cd Education-Management-System-EMS

### Run with Docker

    docker-compose up --build

### Access App

-   API: http://localhost:8000
-   Swagger Docs: http://localhost:8000/api/swagger/
