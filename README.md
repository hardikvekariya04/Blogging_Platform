<<<<<<< HEAD
# Blogging_Platform
=======
# Blog API With JWT Authentication Using Django Rest Framework

# To Run this Project follow below:

mkvirtualenv env
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Postgresql Database setup inside settings.py file

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogging_platform',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Key Features

Custom User Model:
    Uses email and name as unique identifiers.

JWT-Based Authentication and Authorization:
    Secure authentication using JSON Web Tokens (JWT).

Blog Post Management:
    Create, retrieve, update, delete, and search blog posts.

Comment Management:
    Create, retrieve, update, and delete comments on posts.

>>>>>>> a7d91f1 (File uplaod)
