from django.db import models
from django.utils import timezone

# News item model
class Post(models.Model):
    author = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title