# 📝 Django Todo‑App

A simple Todo application built with **Django** to create, view, update, and delete tasks. Ideal for beginners learning Django’s architecture and best practices.

---

## 📂 Repository Contents

* `manage.py` — Django project management script
* `todo/` — Django project configuration (settings, URLs, etc.)
* `todoapp/` — Core application with models, views, URLs, and logic
* `templates/` — HTML templates for the frontend
* `requirements.txt` — List of Python dependencies (to be added)

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/dhakalnirajan/todo-app-django.git
cd todo-app-django
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn’t exist yet, create it with:
> `pip freeze > requirements.txt`

### 4. Set up the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. (Optional) Create superuser

```bash
python manage.py createsuperuser
```

Access the admin panel at: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

### 6. Run the development server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to use the app.

<br>

## Application UI

### 📝 Adding a Task
![Form to add a new task in Zentask](./IMG/zentask%20ss1.png)

### ✅ Task Marked as Completed
![Task shown in completed tab after marking as done](./IMG/zentask%20ss2.png)

### 🧹 Clearing Completed Tasks
![User clearing all completed tasks using clear button](./IMG/zentask%20ss3.png)

### 📭 After Tasks Are Cleared
![Empty state of the UI after clearing completed tasks](./IMG/zentask%20ss4.png)


---

## 📋 Features

* **CRUD operations** for todos
* Mark tasks as completed
* Django template rendering with inheritance
* Admin panel support via `admin.py`

---

## 📐 Project Structure

```
todo-app-django/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── templates/
│   └── index.html
├── todo/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── todoapp/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
└── README.md
```

---

## ✅ Setup Scripts (Optional)

Create these for easier setup:

### `setup.sh` (macOS/Linux)

```bash
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make it executable:

```bash
chmod +x setup.sh
```

### `setup.bat` (Windows)

```bat
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🧹 .gitignore Suggestions

Ensure the following are ignored:

```
venv/
__pycache__/
*.py[cod]
db.sqlite3
.env
```



## 🛠️ Future Improvements

* Add **user login/registration** for personal task lists
* Use **Bootstrap/Tailwind** for responsive UI
* Add **search, filter, and pagination**
* Build a **REST API** with Django REST Framework
* Deploy using **Docker**, Heroku, or Render



## 📬 Feedback

Feel free to open issues or submit PRs to improve this project! Contributions are welcome.
