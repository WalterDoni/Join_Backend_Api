from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class ContactModel(models.Model):
    name = models.CharField(max_length = 100, default = "Max Mustermann")
    email = models.CharField(max_length = 100, default = "Max@Musteremail.at")
    phonenumber = models.CharField(max_length = 100, default = "0123456")
    short = models.CharField(max_length = 5, default = "MM")
    iconColor = models.CharField(max_length = 20, default = "#FF7A00")
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return f'({self.id}) {self.name}'
    
    
class TaskModel(models.Model):
    category = models.CharField(max_length=100, default="No category")
    color = models.CharField(max_length=30, default="0038FF")
    description = models.CharField(max_length=300, default="No description")
    iconColor = models.JSONField(max_length=1024, blank=True)
    id = models.IntegerField(primary_key=True)
    members = models.ManyToManyField(ContactModel)
    priority = models.CharField(max_length=30, default="low")
    section = models.CharField(max_length=50, default="taskCategoryInProgress")
    subtask = models.JSONField(max_length=1024, blank=True)
    title = models.CharField(max_length= 300 , default="No title")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return f'({self.id}) {self.title}'
     