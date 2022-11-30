from django.urls import path
from . import views
# The List of Urls

urlpatterns = [
    path('', views.index , name='index'),
]