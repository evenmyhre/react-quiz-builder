from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length = 50)
    owner = models.ForeignKey('auth.User', related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model): 
    question = models.CharField(max_length = 255)
    questionType = models.CharField(max_length = 255)
    incorrectAnswer1 = models.CharField(max_length = 255, blank=True)
    incorrectAnswer2 = models.CharField(max_length = 255, blank=True)
    incorrectAnswer3 = models.CharField(max_length = 255, blank=True)
    correctAnswer = models.CharField(max_length = 255)
    questionTopic = models.ForeignKey(Topic, related_name="questions")
    owner = models.ForeignKey('auth.User', related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.question