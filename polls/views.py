# from django.http import Http404
from django.http import HttpResponseRedirect
# this template imprt loder no need because of sort hand code of rander at index return time
# from django.template import loader #its for loding html temples
from django.shortcuts import get_object_or_404, render
# this library need when html page have form also need HttpResponseRedirect for the same
from django.utils import timezone

from django.urls import reverse
# use for generic view after modifyed the models.py in Tutorial 4
from django.views import generic

from .models import Choice, Question


# Create your views here.
# time to get reall data from db by importing the Question from models first
# in tutoral 4 change the def name from index to IndexView and arguent request with generic.ListView same for all def
class IndexView(generic.ListView):
    # use in tu 4
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ return the latest five question """
        return Question.objects.order_by('-pub_date')[:5]
    # fetch qustion list order by date limit 5 by this line
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html') #this line also removed because of sort of render
    # context = {
        # 'latest_question_list' : latest_question_list,
    # }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    # sort form of the above reutn render
    # return render(request, 'polls/index.html', context)

# here i'm going to create few more videw to see the questins chocies and votes
# Note - after creating new vies def here must link them on polls urls.py page 


# requsting for the perticular qustions by passing request by question id which pass through the HttpResponse.
# this proces is somting lookes like c printf
class DetailView(generic.DetailView):
    # in tu 4 changes
    model = Question
    template_name = 'polls/detail.html'
    # using try except in case of find wrong case
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exists')
    # above try except used but also have sort use by new 404 library get_object_or_404
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question':question})

# know fetch the question response here
class ResultsView(generic.DetailView):
    # change in tu 4
    model = Question
    template_name = 'polls/results.html'
    # commendt in tu 4
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question': question})

# get vote info
def vote(request, question_id):
    model = Question
    template_name = 'polls/results.html'
    # change in tu 4
    # made commendt in tu 4
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question form in this case
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select the choice",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect agter successfully dealing
    #     # with post data in case you return so prevent to enter dublicate data by this
    #     # user hits back and submit button
    #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

