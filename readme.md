# Django Demo Project to understand better at eas

## Hey if you want to complete your project and need help to complete it. Contact at given email id.
## Contact For College Project / Project Report / Documentation / Project Training @ heykyakaru@gmail.com

## YouTube Videos and related Playlist Details which helps to better understand the code on heyKyaKaru channel

1. [YouTube Channel Link - Python Tutorial Couse Hindi Vido](https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/featured)
2. [Python Couse in Hindi Playlist YouTube - Python Tutorial Couse Hindi Vido](https://www.youtube.com/watch?v=hFbJRORzPK8&list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3)
3. [Tips and Tricks for Programming Playlist YouTube - Python Tutorial Couse Hindi Vido](https://www.youtube.com/watch?v=vPL6ODrfcwI&list=PLK6wiPavf7QiVLYXrC2TW_fdcZp57MgMB)
4. [PHP Projects Playlist YouTube - Python Tutorial Couse Hindi Vido](https://www.youtube.com/watch?v=aMVVRYaT_NA&list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B)
5. [About Our Platform Playlist YouTube - Python Tutorial Couse Hindi Vido](https://www.youtube.com/watch?v=pWEUg4AdbV0&list=PLK6wiPavf7QhMIbSQH56_qgtMvl30TSmj)
6. [Live Python Couser in Hindi Playlist YouTube - Python Tutorial Couse Hindi Vido](https://www.youtube.com/watch?v=W1s0cdaYOa0&list=PLK6wiPavf7QgnXqPf9jBEVr1iNUxiVoHG)



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

## 1. For installing django steps (on vs code you use Terminal which you start by `ctrl+``)

a. Create one directory mkdir newdirecroty

b. Move on to that directory by your cmd and by `cd newdirectory`

c. Run `django install - pip` install Django

d. Create your project by - `django-admin startproject projectname` . After this the admin created with the file sturcte

    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py

e. Go into the `cd projectname` folder

f. Now you created your project for checking it's run properly run `python manage.py runserver`

h. After running it's not auto open on your browser. For this you see the IP on your terminal which you copy past on browser to run the page

## 2. Edit settings on main root folders setting.py

a. Change time-zone to your local zone
`TIME_ZONE = 'Asia/Kolkata'`

b. Set static root folder where you can store your `css/js/image` files. This folder you create
with the same `static` on your root folder.

After that go on setting.py on root. This code you fount on this page at bottom
`STATIC_ROOT = os.path.join(BASE_DIR, 'static')`

Just before this line past or write this one
    `STATIC_URL = '/static/'`

c. Set host at top of page with this if your ip address this when you start your server is show
    on the browser

`ALLOWED_HOSTS = ['127.0.0.1']`

 Dont' add any thing else like may you see the `127.0.0.1:8000` but only add main IP otherwise you get error on your terminal

## 3. After this need to connect with mysql by default Django provides default mysqlLite which is also good but in our case we are going to use mysql

### For connecting with mysql follow these steps

1) I'm using `XAMPP servers MySql`, so for this go to creat on database on `phpmyadmin`
2) I already have this below file on root folder by the name of `mysqlclient-1.4.6` which have `2 version 32 bit and 64 bit` find your suit one by those to or download on form the below link.
Go to this site [mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient) and download the recent `mysqlclient` as per `system bit 32/64`.
3) Past the file on root folder of prject
4) Then run the command - `pip install mysqlclient-1.4.6-cp38-cp38-win32.whl` in my case the file name is this. After successfully install this. Then add the credincials on setting.py file.
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
7) Then at last if get no error on the time of runserver then the last commant which creates table on your connected database -
    1) Command is - `python manage.py migrate`
    2) After this auto create many tables on database

## 4. How to create and connect your app

1) It's very easy app is foldabel and moveable to any were and in any project. Don't focus on this for now because after few time of using the Django you automaitcally understand this concept.
2) For installing the app run following command by having on your root directory which is in my case main folder name is `Mydjango` and then run this cmd - `python manage.py startapp polls`

        After that you found this sturcture on your main folder

        polls/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            views.py
3) Django follow the MVT (`Model=Database View=Controller Templete=HTML`). For html templete folder is not't auto created on the polls folder but we willl creat it after get the apps root structe. For this just ned to creat on new folder with name of `template` on `polls folder`. For more information about the [MVT Click here]<https://pythonistaplanet.com/difference-between-mvc-and-mvt/>
4) In file structe each file is important for know understand the breief of every files
    1. view.py file = This file is same as controller and for this have some steps which needs to follow here.
    For now add the following code into view.py file

            polls/views.py

            from django.http import HttpResponse


            def index(request):
                return HttpResponse("Hello, world. You're at the polls index.")

            Note: This is just basic example but for running this you need to link this with url routing sytem and for that you need to follow below steps.
        1. for using view.py must need a urls.py file in polls root directry wich not have here. SO first need to creat this file.
        2. On urls.py file past this code

                polls/urls.py

                from django.urls import path

                from . import views

                urlpatterns = [
                    path('', views.index, name='index'),
                ] 
        3. After that also inform about this `polls/urls.py` to main root folders `yoursites/urls.py` where your need to import this and add the url on `urlpatterns` after this the `yoursites/urls.py` lookes like this

                mysite/urls.py

                from django.contrib import admin
                from django.urls import include, path

                urlpatterns = [
                    path('polls/', include('polls.urls')),
                    path('admin/', admin.site.urls),
                ]

                Note: The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.
        4. After these change run server cmd to check is every thins runs and you will see the output on browse or not. cmd - `python manage.py runserver`

                Go to http://localhost:8000/polls/ in your browser, and you should see the text “Hello, world. You’re at the polls index.”, which you defined in the index view.
    2. models.py file for handeling database which we better understand at belows definintions.
    3. apps.py file is which use for app also be more know about it at below
    4. admin.py is use to made connection with admin panel and front end panel. We more know about this at below to.

            Note: There is many ohter changes alos which we know in upcoming lines step by step.
5) In app have model.py file which is actually a file which handel all database work here same like mvc's model
6) Great part is model.py auto create db table by the name of class which creates in model

## models.py page to change on it

1) On models.py file added new models or classes `Question` and `Choice` which is aleray on project. But at firest added these on it.

        Note: model is made codeing easy because its models name like Question will also became database table name and the fields on the models also became the tables column. Which is realy great part.
        And that's how pyhone and Django became so easy
2) Also in class all form fields which I define is db tables column fields also that's why at the time of defineing the variable here with datatype and length
3) After creating your class need also need to add /include your app in `root->setting.py` on

    `INSTALLED_APPS = [
        'polls.apps.PollsConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]`
My app which add here where the polls is my app folder name Apps is file in this folder with name of apps.py PollsConfig is in app folder have apps.py folder in which have this class

        Note: After adding the app here Djano know now about the app and use it with admin also.
4) After all this run this

    `python manage.py makemigrations polls`

    Pasted from <https://docs.djangoproject.com/en/3.0/intro/tutorial02/>
    For more information about after this setpes are present here <https://docs.djangoproject.com/en/3.0/intro/tutorial02/>
5) When you run upper cmd if everyting going right then you will the this on your termianl
    `Migrations for 'polls':
    polls/migrations/0001_initial.py:
        - Create model Choice
        - Create model Question
        - Add field question to choice`
6) Last cmd to made magic happence `python manage.py sqlmigrate polls 0001`. When you run this on terminal you will see the output where have noraml mysql querys which done the rest work on behalf of you.
7) Still you didn't see the new tables on your database because sitll on last cmd is pending which is `python manage.py migrate` This cmd alwas mad last changes on db.

        Note: If check your database which have many tables on it but polls/models.py class not became table yet because we don't makemigrations yet but after running the avove cmd models.py all class became tabe on database and also in class fields became column on table. After this command.

## Basic of mysql query on pyhon way

1. At first we do that on shell so for this run this cmd to change youer terminals default cmd to shell of pyhon for running these cmd - `pyhon manage.py shell`
2. After you successfully enterd on shell then try to run these commands line by line on your shell to become familier with these quese which we run on code. But first try these here.

        >>> from polls.models import Choice, Question  # Import the model classes we just wrote.

        # No questions are in the system yet.
        >>> Question.objects.all()
        <QuerySet []>

        # Create a new Question.
        # Support for time zones is enabled in the default settings file, so
        # Django expects a datetime with tzinfo for pub_date. Use timezone.now()
        # instead of datetime.datetime.now() and it will do the right thing.
        >>> from django.utils import timezone
        >>> q = Question(question_text="What's new?", pub_date=timezone.now())

        # Save the object into the database. You have to call save() explicitly.
        >>> q.save()

        # Now it has an ID.
        >>> q.id
        1

        # Access model field values via Python attributes.
        >>> q.question_text
        "What's new?"
        >>> q.pub_date
        datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

        # Change values by changing the attributes, then calling save().
        >>> q.question_text = "What's up?"
        >>> q.save()

        # objects.all() displays all the questions in the database.
        >>> Question.objects.all()
        <QuerySet [<Question: Question object (1)>]>`
3. At last commend `objects.all()` not feching all on privew way so for that change on `polls/models.py` and add def
        `polls/models.py¶
        from django.db import models

        class Question(models.Model):
            # ...
            def __str__(self):
                return self.question_text

        class Choice(models.Model):
            # ...
            def __str__(self):
                return self.choice_text`
4. After that also addind few more custome methods on `polls/models.py` file.

        Note: Like you know that python have librarys for everythins so same that doind here for everythind we need librarys which we can import.
        In this cas I need timezone for that i add this line on models.py file

        from django.utils import timezone
5. Same like shell command on `Djangos` home website also have many sehll cmd which we can not needs yet so I'm left that and mover forward.

## Creat User for Admin Access

1. At first if you try to hit the `ip address/admin/` you get the login panel but for that you must have login credential which you don't get from any where. You need to create one.
2. ss

## Steps to change existing git user on vs code by these steps

1. In case of your if you want to change your remote access from one user to another so it's go by changing on you vs code the git global user name and email by running this cmd -> git config --global user.name "yourname" and same for email
2. After that chack how many remote you added previously on your localsystem of the project by
    git remote -v which show you all remote repository which you added

    If you have non used repository here then simply remove this by
    ctrl+shift+p and type git: remove remote
    After that you show the drop-down of all existing remotes here and remove form here which of those which you don't want
3. If your new remote repository not yet added on local system then add that by the same way and commit fisrt change to check it's working or not
