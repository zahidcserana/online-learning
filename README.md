# Online Learning Platform

## Run in Docker
- docker-compose up
- docker exec -it django bash

## Run without Docker
- python -m venv venv
- venv\Scripts\activate (win)

## Database setup
Set the DB name in tutorial\settings.py (left if using docker)

## start project
- pip3 install -r requirements.txt (left if using docker)
- python manage.py makemigrations 
- python manage.py migrate 

## User setup
(left if using docker)
#### password: admin
- python manage.py createsuperuser --username admin --email admin@example.com 

## Run the project
(left if using docker)
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


## More commands 
- pip freeze > requirements.txt
- docker exec -it pgdb psql -U postgres