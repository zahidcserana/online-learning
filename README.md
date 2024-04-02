# (Online Learning Platform.)

## virtual environment set up
- python -m venv venv


## Activate the virtual environment:
- venv\Scripts\activate
- source venv/bin/activate 
- pip3 install -r requirements.txt

### (pip freeze > requirements.txt)


python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
python manage.py runserver


## Unit Tests

python manage.py test


## To check test coverage
pip install coverage
coverage run manage.py test
coverage report