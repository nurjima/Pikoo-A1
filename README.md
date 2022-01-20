# ToDo app with User authentication using Django
The task was to build a ToDo List app with user authentication (login/registration) using Django Web Framework: 

- Todo list is stored in the Database (DB). As database was used Postgresql.

- Used django ORM to interact with DB

- Used authentication module provided by Django
______________________________________________________________________________________________

Done by Shaliyeva Nurzhamal from SE-2012

## Installation
#### django
```
$ pip install pyjwt
```

#### psycopg. It's needed to connect with PostgreSQL DB
```
$ pip install psycopg2
```
***Note:** If it is not working try this:*
```
$ pip install psycopg2-binary
```

***Note:** If you are a MAC/Linux User type 3, after keywords - pip and python*

## Usage

Install packages, that was mentioned before. Connect with database.
If you are PostgrteSQL user -> change info in settings.py in project folder. 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<name_of_database>',
        'USER': '<username>',
        'PASSWORD': '<your_password>',
        'HOST': '<host>',
        'PORT': '<port>',
    }
}
```
In case, you use databases like SQLite etc., check the django documentation - https://docs.djangoproject.com/en/4.0/

### MacOS
```
python3 manage.py runserver
```

### Windows
```
python manage.py runserver
```

## Examples
Registration Page:

<img width="521" alt="Screen Shot 2022-01-20 at 13 39 12" src="https://user-images.githubusercontent.com/74738634/150294331-d7a39f03-09d2-4968-a154-0678227a16ae.png">


Login Page:

<img width="487" alt="Screen Shot 2022-01-20 at 13 39 34" src="https://user-images.githubusercontent.com/74738634/150294381-4f3d578d-4fbd-4a6f-824d-6d9a7e9c6dfd.png">


Tasks List Page. It has following functionalities - search field, logout button, create/update/delete task, number of incompleted tasks:

<img width="478" alt="Screen Shot 2022-01-20 at 13 40 40" src="https://user-images.githubusercontent.com/74738634/150294519-7b546804-7e1d-4d4a-a9f7-713b5be56341.png">


Search field:

<img width="476" alt="Screen Shot 2022-01-20 at 13 42 32" src="https://user-images.githubusercontent.com/74738634/150294742-1bf1cd90-dce4-411a-a2c3-a330871c6e2e.png">


Task Update Page:

<img width="471" alt="Screen Shot 2022-01-20 at 13 42 11" src="https://user-images.githubusercontent.com/74738634/150294697-f1b9d0f1-6902-45c0-b9f3-8834ded5d012.png">


Task Delete Page:

<img width="467" alt="Screen Shot 2022-01-20 at 13 42 52" src="https://user-images.githubusercontent.com/74738634/150294811-589be52b-38b9-4550-a9d1-95bc7887ffe5.png">
