from django.urls import path
import polls.views as views

urlpatterns = [
    path('',views.index, name='index'),
    path('polls/<int:question_id>/',views.detail, name='detail'),
    path('<int:question_id>/results/',views.result, name='result'),
    path('<int:question_id>/votes/', views.vote, name='vote'),
]