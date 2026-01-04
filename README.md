# Django Blog Application

A feature-rich, multi-role blogging system built with Django. This project was developed by following the course by **Tech With Rathan** and then **customized and hand-coded independently** to deepen my understanding of Django’s architecture, authentication system, permissions, and database management.

The primary goal of this project was **learning by implementation**, not just following tutorials.

---

## 🚀 Features

### 🔐 Multi-Role System

* Granular access control using **Django Groups & Permissions**
* Roles supported:

  * Admin
  * Manager
  * Editor

### 📝 CRUD Functionality

* Full **Create, Read, Update, Delete** operations for:

  * Blog Posts
  * Categories

### 📊 Custom Dashboards

* Role-based dashboards for:

  * Managers
  * Editors
* Content management and basic site statistics

### 💬 Comment System

* Interactive comment section
* Restricted to **authenticated users only**

### ⚡ Advanced Features

* Unique slug generation for **SEO-friendly URLs**
* Dynamic search functionality
* Media handling for **featured image uploads**
* Pagination for clean and user-friendly navigation

---

## 🛠️ Tech Stack

### Backend

* Python 3.12
* Django 6.0

### Frontend

* HTML5
* CSS3
* Bootstrap
* Django Crispy Forms

### Database

* SQLite (Development & Production)

### Deployment

* PythonAnywhere

---

## 📸 Screenshots

* Homepage:
  <img width="1919" height="778" alt="image" src="https://github.com/user-attachments/assets/2b0c8663-0e78-4002-889f-d0542f41bdf9" />
  <img width="1913" height="789" alt="image" src="https://github.com/user-attachments/assets/f6239901-08cf-485e-898b-c37641e567bc" />

* Manager/Editor dashboards:
  <img width="1919" height="824" alt="image" src="https://github.com/user-attachments/assets/67eecbe0-bf6f-45eb-8816-83e9847647e1" />
  <img width="1919" height="852" alt="image" src="https://github.com/user-attachments/assets/fc09f485-a09f-4f4a-960e-6f0039db64f9" />


---

## 🌐 Live Demo

🔗 **Live Project:** *https://hassan908.pythonanywhere.com/*

## 💻 Installation & Setup

### Clone the repository

```bash
git clone https://github.com/Hikey908/Django-Blog_Application.git
cd Django-Blog_Application
```

### Create and activate virtual environment

```bash
mkvirtualenv --python=/usr/bin/python3.12 mysite-virtualenv
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Database setup

```bash
python manage.py migrate
python manage.py loaddata blogs_final.json
```

### Run the development server

```bash
python manage.py runserver
```

---

## 👤 About Me

I am an aspiring Django developer focused on deeply understanding Django by building **hand-coded, real-world projects**. This project helped me strengthen my concepts of:

* Authentication & Authorization
* Role-based access control
* Django ORM
* Project structuring and deployment

---

## 🙏 Acknowledgements

* This project was **inspired by Tech With Rathan**.
* Full credit for the original learning material goes to him.
* Youtube link: https://www.youtube.com/watch?v=1-1ePcEDcqI&t=1s

---
