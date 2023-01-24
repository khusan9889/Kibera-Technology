from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    



