from django.db import models
from learners.models import UserAccount
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50,unique=True, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class Question(models.Model):
    question = models.CharField(max_length=250)
    point = models.IntegerField()
    choice_1 = models.CharField(max_length=250)
    choice_2 = models.CharField(max_length=250)
    choice_3 = models.CharField(max_length=250)
    choice_4 = models.CharField(max_length=250)
    correct_choice = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

STAR_CHOICES=[
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),

]
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='reviews')
    Name = models.CharField(max_length=50)
    Comments = models.CharField(max_length=200)
    rating = models.CharField(choices =STAR_CHOICES, max_length =15)
    def __str__(self):
        return self.quiz.title