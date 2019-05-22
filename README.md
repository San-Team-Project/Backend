Doctor on call appoinment Django app
Getting Started
First of all, clone the repo:

git clone https://github.com/San-Team-Project/Backend.git

cd Backend-backend

Dependencies

npm and python3 for dev mode 

Installing & running

npm install

python manage.py migrate

python manage.py runserver

Important note
To use app properly you need to create some doctors in admin panel. To access it, you need to create a superuser. If you run start.sh, you'll be asked for superuser credentials during setup. If you're running in dev mode, just type python manage.py createsuperuser and provide the data.

