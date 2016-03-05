from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime

class QuestionManager(models.Manager):
    def popular(self):
        return self.order_by('-rating')

    def new(self):
        return self.order_by('-added_at')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, null=True,
        on_delete=models.SET_NULL, related_name='questions')
    likes = models.ManyToManyField(User)

    objects = QuestionManager()

    def __unicode__(self):
        return self.title

    def get_url(self):
        return reverse('question-details',
            kwargs={'qid': self.id})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    question = models.ForeignKey(Question, null=True)
    author = models.ForeignKey(User, null=True,
        on_delete=models.SET_NULL, related_name='answers')

    def __unicode__(self):
        return self.text
