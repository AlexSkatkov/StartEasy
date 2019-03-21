from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):                                             # class that will represent our database
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)        # every post has 1 author and author can have many posts
                                                                      # if we delete a user his posts are deleted too

    def __str__(self):
        return self.title