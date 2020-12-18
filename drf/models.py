from django.db import models

# Create your models here.
class Comment(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
