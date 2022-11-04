
from django.http import HttpResponse,request
# Create your views here.
def index(request):
    return HttpResponse('hello world from our side of the polls')
