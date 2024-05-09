# ovaloop-task
This  is a coding task from Ovaloop

### THIS DOCUMENT IS A GUIDE ON HOW TO RUN THIS TASK ON YOUR LOACAL  ENVIRONMENT

## Clone the repo on Github

github url - https://github.com/TRIGAH/ovaloop-task.git

# Run this Command on your terminal

'''
git clone https://github.com/TRIGAH/ovaloop-task.git

'''

## crate a virtual environment 

Use any name you will like to create the Virtual Environment

# Run this Command on your terminal

'''
python -m venv name_of_virtual_environment

or
python3 -m venv name_of_virtual_environment

Example

python -m venv ovaloop_env

'''
## Activate the virtual environmnet

# Run this command

''''

-Windows

.\virtual_environment_name\Scripts\activate.bat

-Mac or Linux
source virtual_environment_name/bin/activate

''''

## Install necessary dependencies

# Run this command

'''

pip install django djangorestframework

'''

## Provision an Sqlite3 database for your application

# Run this command

Make sure your are in the directory where your manage.py file or module is located

'''

python manage.py makemigrations

python manage.py migrate

''''

## Enjoy your the Application

# Run this command

'''

python manage.py runserver

you could change port with (python manage.py runserver port_number)

python manage.py runserver 5000

where 5000 is your port number

'''


# THANK YOU

## WE ARE OVALOOP .... YOUR EVERYDAY BUSINESS SOLUTION
