import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# Notes for me<<<<<<<<<<<<<<<-----------------------------------------
# here each class in this page is actually a models in Django framwork

# Question class will hold all questin and its data
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text

# choice class will handel the question option
class Choice(models.Model):
        question = models.ForeignKey(Question,on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)

        def __str__(self):
            return self.choice_text