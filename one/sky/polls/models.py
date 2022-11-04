import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

# Schema for the Question
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    # The return string in CLI
    def __str__(self):
        return self.question_text
    
    # Presents the Date and Time in CLI
    def was_published(self):
        return self.timezone.now() - datetime.timedelta(days=1)


# Schema for the Choice
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Returns the String in CLI
    def __str__(self):
        return self.choice
    