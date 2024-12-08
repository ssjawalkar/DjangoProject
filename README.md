# Django Login System

This Django project implements a user login system with support for user registration, login, profile management, and CRUD operations via API endpoints. The application uses Django's ORM for database management and supports both HTML templates and JSON-based API responses for Postman testing.

---

## Features
- **User Registration**: Allows users to sign up with `username`, `email`, and `password`.
- **User Login**: Enables users to log in with their credentials.
- **CRUD Operations**:
  - **Create**: Add a new user via API.
  - **Read**: Retrieve all users or a specific user by `username`.
  - **Update**: Modify user details.
  - **Delete**: Remove a user by `username` or `email`.

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- Django 5.1.4
- A code editor or IDE (e.g., VS Code, PyCharm)
- Postman for API testing


python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
