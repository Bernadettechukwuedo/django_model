from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()



