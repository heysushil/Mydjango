# Django Polls App Example with code and Discription

## [Django Intro Documnet Refrence form here](https://docs.djangoproject.com/en/3.0/intro/)

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
2. for geting the admin panel on your project you need to creat admin user for this follow these cmd
`python manage.py createsuperuser`
Enter your desired username and press enter.

    Username: admin
You will then be prompted for your desired email address:

    Email address: admin@example.com
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

        Password: **********
        Password (again): *********
        Superuser created successfully.
3. Start the development server

    First need to start server by cmd - `python manage.py runserver`

    Now, open a Web browser and go to “/admin/” on your local domain – e.g., <http://127.0.0.1:8000/admin/.> You should see the admin’s login screen:

        Note: As per above app creating there was 2 methods on models.py which is Question and Choice and here you will see the Question where you can already have functionality of add/edit/update/delete facility

        Note: Rest changes will on goin into project files which you download or clore form here.

4. For provideing access to admin panel about the poll app then in polls/admin.py need to import admin and Question method by this

        polls/admin.py

        from django.contrib import admin

        from .models import Question

        admin.site.register(Question)

## Start Polls app

[Django Poll App More Details](https://docs.djangoproject.com/en/3.0/intro/tutorial03/)

1. When I'm getting to add 3 def on views.py
    1. `detail/results/vote` then must add them on
    2. `polls/urls.py` for link it to the routing which is Djangos main part and always follow this.
    3. For adding these def on `polls/urls.py` import
        1. `django.urls path` and
        2. `from . import views`
        3. Then on `urlpatterns` add these 3 paths with url behaviour like
            1. Example For single poll - `http://IP_Address/polls/question_id/` or for single question `http://IP_Address/polls/question_id/results/` like that.
2. In views.py of accessing `HttpResponse` need to import
    1. `from django.http import HttpResponse`
    2. For models.py `Question` also import the model here `from django.http import HttpResponse`
    3. Because like the normal function which request for somthins and when fucntion get that then must response for this in the form of `return`. So the same pictures goes here.
    4. For more details look at this

            polls/views.py¶
            from django.http import HttpResponse

            from .models import Question

            def index(request):
                latest_question_list = Question.objects.order_by('-pub_date')[:5]
                output = ', '.join([q.question_text for q in latest_question_list])
                return HttpResponse(output)

            # Leave the rest of the views (detail, results, vote) unchanged

3. On views.py page all code is hard coded for know but we need HTML to represent this. And at first we don't get that.
    1. In `Django` html codes are holdes in `templates` folder and for theat created one in `polls/templates`
    2. After that must inform the `Django` framwork about this folder which form for html templates by following way.
        1. `Polls` is app but main core power is holds by the `root folders files`. So confirm that we need to inform about templates to the `root`.
        2. But first if we have `Polls App` then for this app realated all html files will stroe in `polls/templates/polls/index.html` like way. It's import to create `polls` folder in `templates`
        3. After creating `index.html` in `polls/templates/polls/` then `import` this in views.py file by `from django.template import loader`.
        4. Know views.py def index lookes like

                def index(request):
                    latest_question_list = Question.objects.order_by('-pub_date')[:5]
                    template = loader.get_template('polls/index.html')
                    context = {
                        'latest_question_list': latest_question_list,
                    }
                    return HttpResponse(template.render(context, request))

    3. `Django` have sortcut of `HttpResponse` is `render` which works the same so now change the views.py like this by importing `from django.shortcuts import render`

            from django.shortcuts import render

            from .models import Question


            def index(request):
                latest_question_list = Question.objects.order_by('-pub_date')[:5]
                context = {'latest_question_list': latest_question_list}
                return render(request, 'polls/index.html', context)

            Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

            The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

4. Raising a 404 error in views.py

        Note: We now very well all the import alwas goes through conterller and in `Django's` case controller is views.py

    1. We know than if not found the url then show error page and this is for this.
    2. Import `from django.http import Http404` after that views.py `detail model` looks like

            from django.http import Http404
            from django.shortcuts import render

            from .models import Question
            # ...
            def detail(request, question_id):
                try:
                    question = Question.objects.get(pk=question_id)
                except Question.DoesNotExist:
                    raise Http404("Question does not exist")
                return render(request, 'polls/detail.html', {'question': question})

    3. Sortcute of `Http404` is `get_object_or_404` after replacing this the views.py code

            from django.shortcuts import get_object_or_404, render

            from .models import Question
            # ...
            def detail(request, question_id):
                question = get_object_or_404(Question, pk=question_id)
                return render(request, 'polls/detail.html', {'question': question})
            
            Note: The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.

    4. Then created detail.html file where you look the pyhon and html syntex are at first looks confuging but after that it's easy for you.
5. Namspace for deffernciate `Django's` multiple `apps` same `models`
    1. The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? For example, the polls app has a detail view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?
    2. The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace:
    3. For this on polls folders urls.py file add the name of app like this

                polls/urls.py

                from django.urls import path

                from . import views

                app_name = 'polls'
                urlpatterns = [
                    path('', views.index, name='index'),
                    path('<int:question_id>/', views.detail, name='detail'),
                    path('<int:question_id>/results/', views.results, name='results'),
                    path('<int:question_id>/vote/', views.vote, name='vote'),
                ]

6. At last modifyed the index.html because when we define the app name on `polls/urls.py` it make templates easy to connect with views.py models. for that need to change the way of calling url on html file like this in `index.html` page

        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>

## Writing your first Django app, part 4 as per Django website

1. Use generic views: Less code is better in this part shows the minimization of code on views.py file.
2. Changed the def with classes on views.py file.
3. CHanges are following
    1. In views.py file def was defauls but now created class with class name with have `template name` which we use for that class also `model name` which we use to get the data.
    2. After defining class in views.py file then in `polls/urls.py` file change the `urlpatterns` of each.
    3. And the `templates` file are same as pre. but you once look at those file.
    4. Know it makes real seens from here becasue we are more habuchual with class which know part of views.py
    5. Also in views.py file in class pass a `argument` which for import a `generic` library also in class pass 2 type of arguments
        1. `ListView` = Abstruct the concept of `display a list of objects`
        2. `DetailView` = Abstruct the concept of `display a detail page for particular type of object`. DetailView want's a primary key to show the single object. For that pass a `pk` in `polls/urls.py` file in urlpatterns
        3. Each of them use `generic` before them which is use for know about model. Means each `generic` view which model using by this acting upon that model
        4. For more understanding about this concept learn [Django Tutorail 4](https://docs.djangoproject.com/en/3.0/intro/tutorial04/)

## Django Part 5 - About Test case in polls/tests.py

1. Test cases are use similer like's validation but it work some extra graet way. Because test cases stop the `loop hols of functionality`.
2. For that right a individual `def test cases` in tests.py file which helps to check the functionality at once of full app by running this cmd - `python manage.py test polls` which show the test case in terminal with problem and line in which the problem arries.
3. Test case also reduce the problem of test it work to handel full apps testing at once.
4. For info abotu test case look at this [Django Tutorail 5](https://docs.djangoproject.com/en/3.0/intro/tutorial05/)

## Steps to change existing git user on vs code by these steps

1. In case of your if you want to change your remote access from one user to another so it's go by changing on you vs code the git global user name and email by running this cmd -> git config --global user.name "yourname" and same for email
2. After that chack how many remote you added previously on your localsystem of the project by
    git remote -v which show you all remote repository which you added

    If you have non used repository here then simply remove this by
    ctrl+shift+p and type git: remove remote
    After that you show the drop-down of all existing remotes here and remove form here which of those which you don't want
3. If your new remote repository not yet added on local system then add that by the same way and commit fisrt change to check it's working or not
