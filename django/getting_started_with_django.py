#Django 
#python most popular web framework , a set of tool designed for building interactive web applications.
#project- Learning Log (an online journal system that lets you keep track of information you've learned about particular topics.)
#writing spec
#spec / specification - a document that explains how a project should be completed.

#creating a virtual environment
#A virtual environment is a place on your system where you can install packages for a particular project without affecting the system-wide installation of packages.
# Command python -m venv (name of the virtual environment)
#activate the virtual environment
# Command source name_of_virtual_environment/bin/activate - this command runs the script activate in the bin directory of the virtual environment.
# to stop the virtual environment, use the command deactivate


#installing Django
# command pip install --upgrade pip - to upgrade pip its advisable to upgrade pip whenever you make a new environment
# command pip install django - to install django


#Creating a new project
# command django-admin startproject (name of the project)  . - the dot at the end of the command tells Django to create the new project with a directory structure that will make it easy to deploy the project to a web server when the time comes.
#startproject - a command that tells Django to set up a new project with the name you specify.
#manage.py file - short program that takes in commands and feeds them to the relevant parts of Django. eg working with database and running servers.
#settings.py file - controls how django interact with your system and manages your project.
#urls.py file - helps django server the files it creates the filename is an acronym for "web server gateway interface"


#Creating the database
#python manage.py migrate - tells Django to make sure the database matches the current state of the project.
#migrating the database - modifying the database
#SQLite iss a database that runs off a single file, ideal for writing simple apps because you wont have to pay much attention managing the database.


#viewing the project
#python manage.py runserver - starts the server(development server) and tells Django to listen for requests on port 8000 on your computer. http://127.0.0.1:8000/ - the address of the server
#you can also specify the port you want to use by adding the port number at the end of the command. eg python manage.py runserver 8001

#starting an app
#a django project is organized as group of individual apps that work together to make the project work as a whole.
#command python manage.py startapp (name of the app)
#the command startapp app name tells django to create the infrastructure needed to build an app.
#models.py file- used to define the data we want to manage in our app .

#defining models
#regarding our learning log app.
#1. each user will need to create a number of topics in their learning log.
#2. Each entry they make will be tied to a topic and these entries will be displayed as text.
#3. store the timestamps of each entry, so we can see when each entry was made.

#a module called models is being imported from django.db
#model tells django how to work with the data that will be stored in the app.
#model is a class , it has attributes and methods .
#syntax class name_of_model(models.Model):  

#ref https://docs.djangoproject.com/en/5.0/ref/models/fields/]

#activating models
#tell django to include our app in the overall project by add the app in the settings.py file in the INSTALLED_APPS section.

#python manage.py makemigrations app_name - tells django to modify the database so it can store information related to the model Topic
#makemigrations - tells django to figure out how to modify the database so it can store the data related to the model we've defined.
#0001_initial.py - the file that django created to store the changes it needs to make to the database.
#apply the changes to the database by running the command python manage.py migrate

#whenever we want to modify the data thats being stored in database or project manages.
#1. modify the models.py file
#2. run the command python manage.py makemigrations app_name
#3. run the command python manage.py migrate


#django admin site
#django makes it easy to work with models through the admin site.
#its is only meant to be used by sites administrators. not meant for regular users.

#setting up a superuser
#superuser - a user who has all the privileges available on the site.
#command python manage.py createsuperuser - tells django to create a superuser for the project.
#django hashes the password for security reasons.


#registering a model with the admin site
#django includes some models in the admin site automatically  such as User and Group. bt models we create needs to be added manually.
#syntax admin.site.register(ModelName) - tells django to manage our model through the admin site.

#defining the entry model
#many-to-one relationship - a relationship where many items are tied to one item.
