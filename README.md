Django Blog Application
This is a feature-rich, multi-role blogging system built with Django. Originally developed following the premium course by Tech With Rathan, I have customized and "hand-coded" the logic to deepen my understanding of Django's architecture, authentication systems, and database management.

🚀 Features
Multi-Role System: Implemented granular access control for Admins, Managers, and Editors using Django Groups and Permissions.

CRUD Functionality: Full Create, Read, Update, and Delete capabilities for blog posts and categories.

Custom Dashboards: Role-based dashboards for Managers and Editors to manage content and view site statistics.

Comment System: Interactive comment section restricted to authenticated users.

Advanced Features: * Unique slug generation for SEO-friendly URLs.

Dynamic search functionality.

Media handling for featured image uploads.

Pagination for clean content navigation.

🛠️ Tech Stack
Backend: Python 3.12, Django 6.0

Frontend: HTML5, CSS3, Bootstrap (Crispy Forms)

Database: SQLite (Development/Production)

Deployment: PythonAnywhere

💻 Installation & Setup
Clone the repository:

Bash

git clone https://github.com/Hikey908/Django-Blog_Application.git
cd Django-Blog_Application
Create and activate a virtual environment:

Bash

mkvirtualenv --python=/usr/bin/python3.12 mysite-virtualenv
Install dependencies:

Bash

pip install -r requirements.txt
Database Setup:

Bash

python manage.py migrate
python manage.py loaddata blogs_final.json
Run the server:

Bash

python manage.py runserver
👤 About Me
I am an aspiring Django developer, currently focused on learning the framework's various aspects and building hand-coded projects.

Support the original creator: This project was inspired by Tech With Rathan. Check out his channel for excellent Django tutorials!
