1. Create Virtual environment through command pallet Python: select environment or through terminal
2. install Django, pip install django
3. Create Django project through command line (django-admin startproject {project_name})



Creating Django app
    1. python manage.py startapp {app_name}
    2. Add app to settings

Create a Superuser
    1. python manage.py createsuperuser
    2. Username
    3. Password
    4. Email
    


Migrating Database
    1. python manage.py migrate
    2. python manage.py makemigrations first_app
    3. python manage.py migrate

Populate Database through shell
    1. python manage.py shell
    2. Import the model from your app ie { from first_app.models import {Model} }

Register Database in admin.py File
    1. import app.models
    2. admin.site.register({Model})