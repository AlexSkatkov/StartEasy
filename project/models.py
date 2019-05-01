from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):                                             # class that will represent our database
    title = models.CharField(max_length=100)
    deadline=models.TextField(blank=True)
    customer = models.TextField(blank=True)
    pro = models.TextField(blank=True)
    goals = models.TextField(blank=True)
    problems = models.TextField(blank=True)
    connection = models.TextField(blank=True)
    yearly_work_plan = models.TextField(blank=True)
    cost_and_prodactivity = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')        # every post has 1 author and author can have many posts
    user1 = models.TextField(blank=True)
    user2 = models.TextField(blank=True)
    user3 = models.TextField(blank=True)
    user4 = models.TextField(blank=True)
    client = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('project.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text