import datetime
from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.CharField(max_length=20000)
    post_date = models.DateTimeField('date published')
    def __str__(self):
        return self.post_title


