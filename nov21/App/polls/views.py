from django.shortcuts import render
from .models import Question, Choice
# Create your views here.

# index
def index(request):
    return render(request, "polls/index.html",{
        "questions" : Question.objects.order_by('-pub_date')
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
def vote(request):
    ...