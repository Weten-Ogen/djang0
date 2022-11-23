from django.shortcuts import render
from .models import Question, Choice
from django.urls import reverse
# Create your views here.

# index
def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, "polls/index.html",{
        "questions" : questions
    })

# details
def detail(request, question_id):
    question =  Question.objects.get(pk=question_id)
    return render(request, "polls/detail.html",{
        "question":question
    })

# results
def result(request, q_id):
    ...

#Votes
def vote(request, question_id):
    question = Question.choice_set.get(pk='question_id')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{
            "question" : question
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return render(request, reverse('poll:result.html',args=(question.id,)))