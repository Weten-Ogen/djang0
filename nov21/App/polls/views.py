from django.shortcuts import render
from .models import Question
# Create your views here.

# index
def index(request):
    q = Question.objects.all()
    return render(request, "polls/index.html",{
        q: "q"
    })

# details
def detail(request, q_id):
    pass

# results
def result(request, q_id):
    ...

#Votes
def vote(request):
    ...