from django.db import models
from django.contrib.auth.models import User
from learners.models import UserAccount

# Create your models here.

class QuizHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    your_choice = models.CharField(max_length=250)
    correct_choice = models.CharField(max_length=250)
    correct_quiz = models.IntegerField(default=0)

    def __str__(self):
        return self.question 
    
    
  