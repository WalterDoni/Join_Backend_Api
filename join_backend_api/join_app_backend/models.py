from django.db import models
from django.contrib.auth.models import User

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
    title = models.CharField(max_length=100, default = "Empty title")
    description = models.CharField(max_length=500, default = "Empty description")
    assigned_to = models.ManyToManyField(ContactModel)
    priority = models.CharField(max_length=100, default = "to-do")
    category = models.CharField(max_length=100, default = "Max Mustermann")
    subtask = models.CharField(max_length=500, default = "nothing")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return f'({self.id}) {self.title}'
     