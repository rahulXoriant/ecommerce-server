# Introduction

The goal of this project is to provide a REST apis using Django Rest Framework that can be used with ecommerce frontend app. 

The application is written with django 3.2.19 and python 3.7.3.
      
# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/rahulXoriant/ecommerce-server
    $ cd ecommerce-server
    $ git checkout dev // to go to the dev branch
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver