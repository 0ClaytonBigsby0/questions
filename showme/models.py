from django.db import models

class ShowMeQuestion(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255, default='default_option')
    option2 = models.CharField(max_length=255, default='default_option')
    option3 = models.CharField(max_length=255, default='default_option')
    correct_answer = models.CharField(max_length=255, default='default_option')

    def __str__(self):
        return self.question