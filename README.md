## Title
Awwadery

## Authour
Hope Mbuthye

 ## Description
project that allows people to display projects they have worked on and get ranked of the best of their projects by peers

 ## Features
User can log in to application and view other peoples projects.

A user can upload projects and edit asew

Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.

## Behavior Driven Development
 # Behavior	Input	Output

User visits the app and gets redirected to the login page	User logs in Directed to the home page where they see posted photos

If user has no account, they click on sign up	User signs up	User is redirected to the log in page
Homepage loads	Click profile	User's profile appears
Homepage loads	Click upload image icon	User's redirected to a page where they can upload an image
Homepage loads	Click settings icon	A modal appears where one can change their password or logout
Homepage loads	User inputs in the search form and presses enter Searched results show
## Setup/Installation requirements

1.Clone or download and unzip the repository from github,https://github.com/hope-mbuthye38/awwardy.git
Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate

## Installation dependacies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

Create the Database

psql
CREATE DATABASE ;
Create .env file and paste paste the following filling where appropriate:
-SECRET_KEY = '<Secret_key>' -DBNAME = 'Awward' -USER = '' -PASSWORD = '' -DEBUG = True 5. Run initial Migration -python3.8 manage.py makemigrations instagram -python3.8 manage.py migrate 6. Run the app -python3.8 manage.py runserver -Open terminal on localhost:8000

## Technologies Used

PYTHON 3.8
DJANGO FRAMEWORK
BOOTSTRAP
CSS
DB.SQLITE3
Prerequisite
PYTHON 3.8
DJANGO FRAMEWORK
PYTHON VIRTULENV

Support and contact details
contact me @ hopembuthye38@gmail.com

 ## License
The project is underMIT license Copyright © 2021.All rights reserved

## About
Application that will allow a user to post a project he/she has created and get it reviewed by his/her peers.

awwwards5.herokuapp.com/
## Resources
Readme.md
Releases
No releases published
Packages
No packages published
## Languages
python  86.9%
Javascript 10.3%
Html 1.7%
css 0.9%
powershell 0.1%
c 0.1%
