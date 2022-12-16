from django.shortcuts import render
from .models import Product
# Create your views here.
def home_view(request):
    return render(request , 'index.html')

def about_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title':obj.title,
        'description':obj.description,
        'price': obj.price,
    }
    return render (request, 'about.html', context)