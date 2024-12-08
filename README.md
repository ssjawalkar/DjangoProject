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
  - **Delete**: Remove a user by `email`.

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- Django 5.1.4
- A code editor or IDE (e.g., VS Code, PyCharm)
- Postman for API testing

```
git clone
cd DjangoLoginSystem

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

pip install django

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```
---

### Screen Shots
#### Login Page
![image](https://github.com/user-attachments/assets/a9a1bc80-4e75-4ef2-926d-1dc301e118bd)

#### Sign Up Page
![image](https://github.com/user-attachments/assets/e6536708-cbe2-4831-a0e3-9e5743931730)



#### Get Users
![image](https://github.com/user-attachments/assets/c379f8e6-374c-4284-b1cb-cb266453334a)

#### Create User 
![image](https://github.com/user-attachments/assets/35ee854a-4ec2-4ca6-92c2-d3880c85e88b)

#### Get User by UserID
![image](https://github.com/user-attachments/assets/160e6f65-3523-45fa-9116-3c8e7fcef13f)

#### Update User
![image](https://github.com/user-attachments/assets/7876e147-4502-4b25-8796-133bf72835bb)

#### Copy User
![image](https://github.com/user-attachments/assets/a484c306-911c-47fc-b894-2055dc525eef)

#### Django Shell
![image](https://github.com/user-attachments/assets/359c01b4-4187-49bb-ae4d-120a31dbe520)
