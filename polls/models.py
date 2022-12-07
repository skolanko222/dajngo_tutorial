from django.db import models

# Create your models here.

class Question(models.Model): # creating models represented by a class
    question_text = models.CharField(max_length = 250) # each class variable correspond to a column
    publication_date  = models.DateTimeField('date')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # associating each Choice with a Question
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)