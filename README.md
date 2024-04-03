# Online Learning Platform

## virtual environment set up
- python -m venv venv


## Activate the virtual environment:
- venv\Scripts\activate (win)
- source venv/bin/activate (ubuntu)

## Database setup
- Set the DB name in tutorial\settings.py

## start project
- pip3 install -r requirements.txt (pip freeze > requirements.txt)
- python manage.py makemigrations 
- python manage.py migrate 

## User setup: 
#### password: admin
- python manage.py createsuperuser --username admin --email admin@example.com 
- python manage.py runserver

## Postman Test
- Base url: http://127.0.0.1:8000
- CRUD Course url: /courses/
- CRUD Enrollment url: /enrollments/
- Authorization: Basic Auth: username,password: admin

- Course data: 
{
    "title": "title5",
    "instructor": "instructor",
    "duration": 55,
    "description": "description",
    "price": 5555
}

- Enrollment data: 
{
    "student": "student",
    "course_id": 2
}

## Unit Tests
- python manage.py test


## To check test coverage
- pip install coverage 
- coverage run manage.py test 
- coverage report