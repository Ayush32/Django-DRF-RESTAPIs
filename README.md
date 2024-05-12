# REST API using Django and DRF for managing the users data

## User has the following attributes

* ID - Do Not need to add ID while creating a new user, ID is Autofield and auto increment, primary key
* First Name
* Last Name
* Company Name
* Age
* City
* State
* Zip
* Email
* Web

### Sample structure
      {
            "first_name": "James",
            "last_name": "Butt",
            "company_name": "Benton, John B Jr",
            "state": "LA",
            "zip": 70116,
            "email": "jbutt@gmail.com",
            "web": "http://www.bentonjohnbjr.com",
            "age": 19
        }

## The application has the following endpoints

* /api/users – GET – To list the users<br>
  Also, supports some query parameters:-

    - page – a number for pagination
    - limit – no. of items to be returned, default limit is 5
    - name – search user by name as a substring in First Name or Last Name (Note, use substring matching algorithm/pattern to match the      name). It should be case-insensitive.
    - Sort – name of attribute, the items to be sorted. By default it returns items in ascending order if this parameter exist, and if     the value of parameter is prefixed with ‘-’ character, then it should return items in descending order
* /api/users – POST – To create a new user
* /api/users/{id} – GET – To get the details of a user with specific id
* /api/users/{id} – PUT – To update the details of a user
* /api/users/{id} – DELETE – To delete the user

## Software
Python = 3.12
Django==5.0.6
djangorestframework==3.15.1
psycopg2==2.9.9


## Step by step guide to run this project

* Download and extract the zip file.
* Open this folder inside VScode
* Open terminal and setup virtual enviroment by following steps

              python -m venv env
              Go to scripts directory then activate the virtual environment - myenv\Scripts\activate
              go back to main directory by using cd.. for windows
              
* Install django, djangorestframework, psycopg2 by following command

              pip install Django==5.0.6 djangorestframework==3.15.1 psycopg2==2.9.9
* Now do run the following command to save your model into the database.

              Go to the backend directory , run below commands 
              python manage.py makemigrations core
              python manage.py migrate
              
* Now run the following command to runserver
  
              Go to the backend directory 
              python manage.py runserver
