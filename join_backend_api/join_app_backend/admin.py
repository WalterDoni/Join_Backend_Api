from django.contrib import admin
from .models import  *

admin.site.register(ContactModel)
admin.site.register(SubtaskModel)
admin.site.register(ColorModel)
admin.site.register(TaskModel)