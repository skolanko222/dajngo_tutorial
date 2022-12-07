from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

def index(request):
    context = {'all_questions' : Question.objects.all()}
    return render(request, 'polls/index.html', context) # a shortcut for rendering templates by HttpResponse

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist): # exception, when no option is choosen
       return  render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",})
    
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results',args = (question.id,)))