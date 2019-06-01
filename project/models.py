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
    Application = models.TextField(blank=True)
    General_Architecture_Highlights = models.TextField(blank=True)
    Current_situation = models.TextField(blank=True)
    System_character = models.TextField(blank=True)
    Constraints = models.TextField(blank=True)
    Glossary = models.TextField(blank=True)
    External_demarcation = models.TextField(blank=True)
    Internal_demarcation = models.TextField(blank=True)
    User_Interface = models.TextField(blank=True)
    Processes = models.TextField(blank=True)
    Code_tables = models.TextField(blank=True)
    Logical_files = models.TextField(blank=True)
    Dictionary_of_information = models.TextField(blank=True)
    Reports = models.TextField(blank=True)
    Data_Security = models.TextField(blank=True)
    Volumes_loads_and_performance = models.TextField(blank=True)
    Interfaces_and_links = models.TextField(blank=True)
    General_Architecture = models.TextField(blank=True)
    Central_hardware = models.TextField(blank=True)
    Environmental_infrastructure = models.TextField(blank=True)
    Database = models.TextField(blank=True)
    Development_and_maintenance_tools = models.TextField(blank=True)
    Shelf_software = models.TextField(blank=True)
    Hardware = models.TextField(blank=True)
    Local_private_communications = models.TextField(blank=True)
    similar_Technologies = models.TextField(blank=True)
    Factors_involved = models.TextField(blank=True)
    Work_Plan = models.TextField(blank=True)
    next_step = models.TextField(blank=True)
    Ongoing_operation = models.TextField(blank=True)
    Service_and_maintenance = models.TextField(blank=True)
    Integration = models.TextField(blank=True)
    Robustness_and_reliability = models.TextField(blank=True)
    Configurations = models.TextField(blank=True)
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