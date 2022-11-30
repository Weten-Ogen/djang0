from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class Entry(models.Model):
    entry = models.ForeignKey(Blog, on_delete=models.CASCADE)
    