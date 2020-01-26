from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title