
from django.db import models
from django.utils import timezone


class Post(models.Model):
    #image
    #author
    title = models.CharField(max_length=200)
    content = models.TextField()
    #tag
    #category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
