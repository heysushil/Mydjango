from django.http import Http404

from django.http import HttpResponse
# this template imprt loder no need because of sort hand code of rander at index return time
# from django.template import loader #its for loding html temples
from django.shortcuts import get_object_or_404,render

from .models import Question

# Create your views here.
# time to get reall data from db by importing the Question from models first
def index(request):
    # fetch qustion list order by date limit 5 by this line
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html') #this line also removed because of sort of render
    context = {
        'latest_question_list' : latest_question_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    # sort form of the above reutn render
    return render(request, 'polls/index.html', context)

# here i'm going to create few more videw to see the questins chocies and votes
# Note - after creating new vies def here must link them on polls urls.py page 

# requsting for the perticular qustions by passing request by question id which pass through the HttpResponse.
# this proces is somting lookes like c printf
def detail(request, question_id):
    # using try except in case of find wrong case
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exists')
    # above try except used but also have sort use by new 404 library get_object_or_404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

# know fetch the question response here
def results(request, question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response %question_id)

# get vote info
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)

