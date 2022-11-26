from django.db import models

# Create your models here.

# Question Schema
class Question(models.Model):
    question_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __repr__(self):
        return f"{self.question_txt} {self.pub_date}"

# Choice Schema
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_txt= models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __repr__(self):
        return f"{self.question} {self.choice_txt} {self.votes}"