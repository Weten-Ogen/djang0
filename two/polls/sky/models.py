from django.db import models

# Create your models here.

# Questions
class Questions(models.Model):
    question_txt = models.CharField(max_length=500)
    published_date = models.DateTimeField(' date published')

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_txt =models.CharField(max_length=200)
    votes =models.IntegerField(default=0)


