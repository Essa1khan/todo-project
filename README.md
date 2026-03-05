# Django ToDo Application

A simple and clean **Task Management (ToDo) web application** built with Django.
The application allows users to create tasks, mark them as completed, and manage daily activities efficiently.

---

## 🚀 Features

* Add new tasks
* Mark tasks as completed
* View pending tasks
* View completed tasks
* Admin dashboard for task management
* Clean Bootstrap UI
* Secure Django form handling (CSRF protection)

---

## 🛠 Tech Stack

**Backend**

* Python
* Django

**Frontend**

* HTML5
* Bootstrap 5
* Font Awesome

**Database**

* SQLite (default Django database)

**Version Control**

* Git
* GitHub

---

## 📁 Project Structure

```
todo-project/
│
├── manage.py
├── db.sqlite3
│
├── todo_main/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
│   └── home.html
│
└── static/
```

---

## ⚙️ Installation Guide

Clone the repository:

```
git clone https://github.com/Essa1khan/todo-project.git
```

Move into the project directory:

```
cd todo-project
```

Create virtual environment:

```
python -m venv env
```

Activate environment:

Windows:

```
env\Scripts\activate
```

Mac/Linux:

```
source env/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run database migrations:

```
python manage.py migrate
```

Start the development server:

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 📸 Application Workflow

```
User Input
     ↓
HTML Form
     ↓
Django View
     ↓
Model (Database)
     ↓
Template Rendering
     ↓
Updated Task List
```

---

## 🧠 Learning Objectives

This project demonstrates:

* Django project structure
* Models and database migrations
* Django admin customization
* Template rendering
* URL routing
* Form handling with POST requests
* CRUD operations

---

## 🔐 Admin Panel

Access Django admin panel:

```
http://127.0.0.1:8000/admin
```

From here you can:

* Add tasks
* Edit tasks
* Delete tasks
* Manage database records

---

## 📈 Future Improvements

* Task editing functionality
* Task deletion from UI
* User authentication
* REST API integration
* PostgreSQL database
* Deployment with Docker
* Live hosting

---

## 👨‍💻 Author

**Muhammad Essa Khan**

* AI & Software Developer
* University of Peshawar
* GitHub: https://github.com/Essa1khan

---

## ⭐ Support

If you like this project, please consider giving it a **star on GitHub** ⭐

It helps others discover the project and motivates further development.
