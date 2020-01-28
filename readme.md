# Django Demo Project to understand better at eas

Hello welcome to this project. It's for beginer because I'm also the beginer when I started this
But I just started the prectice this way so it not just hepl me but also others to.
I'm trying to make it easy and if others may include thier contribution on this then it will
also very better. There is everything but first thing first.
At first I'm describe how to install Django and setup it

I'm using visual studio code editor for it.
If you don't have much expericne of it no wory just gave it your full day to understand then it
will be your first choice of editor but first you must understand the editor to work on it.
Because Microsoft put a grate effort on it to make it very user friendly for developers also
the best part of the vs code is it's have spacial features for pyhon and it's related library.

So you must consider this at begging of your python and Django.

This is also my first Django app so I also follow the tutorial of Django site.

## 1. For installing django steps (on vs code you use Terminal which you start by ctrl+`)

    a. Create one directory mkdir newdirecroty
    b. Move on to that directory by your cmd and by cd newdirectory
    c. Run django install - pip install Django
    d. Create your project by - django-admin startproject projectname
    e. Go into the cd projectname folder
    f. Now you created your project for checking it's run properly run python
    manage.py runserver
    h. After running it's not auto open on your browser. For this you see the IP
    on your terminal which you copy past on browser to run the page

## 2. Edit settings on main root folders setting.py

    a. Change time-zone to your local zone
    TIME_ZONE = 'Asia/Kolkata'
    b. Set static root folder where you can store your css/js/image files. This folder you create
    with the same "static" on your root folder.

    After that go on setting.py on root. This code you fount on this page at bottom
    i. STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    Just before this line past or write this one
        STATIC_URL = '/static/'

    c. Set host at top of page with this if your ip address this when you start your server is show
     on the browser

    ALLOWED_HOSTS = ['127.0.0.1'] Dont' add any thing else like may you see the '127.0.0.1:8080' but only add main IP otherwise you get error on your terminal

## d. After this need to connect with mysql by default Django provides default mysqlLite which is also good but in our case we are going to use mysql

    i. For connecting with mysql follow these steps
    1) I'm using XAMPP servers MySql, so for this go to creat on database on phpmyadmin
    2) I already have this below file on root folder by the name of
        mysqlclient-1.4.6 which have 2 version 32 bit and 64 bit find your suit
        one by those to or download on form the below link.
        Go to this site https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient and download
        the recent mysqlclient as per system bit 32/64.
    3) Past the file on root folder of prject
    4) Then run the command - pip install mysqlclient-1.4.6-cp38-cp38-win32.whl  |||in my
        case the file name is this
    5) In root folders setting.py at database section add these lines

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'mydjango',
                'USER': 'root',
                'PASSWORD':'',
                'HOST':'localhost',
                'PORT':'3306',
            }
        }

    6) Port is mysql port which you get on xampp servers mysql section
    7) Then at last if get no error on the time of runserver then the last commant which
        creates table on your connected database -
            a) Command is - python manage.py migrate
            b) After this auto create many tables on database

## How to create and connect your app

    1) It's very easy app is foldabel and moveable to any were and in any project. Don't focus on this for now because after few time of using the Django you automaitcally understand this concept.
    2) In app have model.py file which is actually a file which handel all database work here same like mvc's model
    3) Great part is model.py auto create db table by the name of class which creates in model
    4) Also in class all form fields which I define is db tables column fields also that's why at the time of defineing the variable here with datatype and length
    5) After creating your class need also need to add /include your app in root->setting.py on

        INSTALLED_APPS = [
            'polls.apps.PollsConfig',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]

    Like the yellow part which is my app which add here where the polls is my app folder name Apps is file in this folder with name of apps.py PollsConfig is in app folder have apps.py folder in which have this class
    6) After all this run this

        python manage.py makemigrations polls

        Pasted from <https://docs.djangoproject.com/en/3.0/intro/tutorial02/>

    7) For more information about after this setpes are present here https://docs.djangoproject.com/en/3.0/intro/tutorial02/

## Steps to change existing git user on vs code by these steps

    1. In case of your if you want to change your remote access from one user to another so it's go by changing on you vs code the git global user name and email by running this cmd -> git config --global user.name "yourname" and same for email
    2. After that chack how many remote you added previously on your localsystem of the project by
        git remote -v which show you all remote repository which you added

        If you have non used repository here then simply remove this by
        ctrl+shift+p and type git: remove remote
        After that you show the drop-down of all existing remotes here and remove form here which of those which you don't want
    3. If your new remote repository not yet added on local system then add that by the same way and commit fisrt change to check it's working or not
