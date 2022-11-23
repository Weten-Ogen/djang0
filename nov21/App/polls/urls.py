from django.urls import path
import polls.views as views

app_name = ''
urlpatterns = [
    path('',views.index, name='index'),
    path('polls/<int:question_id>/',views.detail, name='detail'),
    path('polls/<int:question_id>/results/',views.result, name='result'),
    path('polls/<int:question_id>/vote', views.vote, name='vote'),
]