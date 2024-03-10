from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    incorrect_answer1 = models.CharField(max_length=200)
    incorrect_answer2 = models.CharField(max_length=200)
    incorrect_answer3 = models.CharField(max_length=200)
    image = models.ImageField(upload_to='questions_images/', blank=True, null=True)

