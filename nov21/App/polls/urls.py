from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:q_id>/',views.detail, name='detail'),
    path('<int:q_id>/results/',views.result, name='result'),
    path('<int:q_id>/votes/', views.vote, name='vote'),
]