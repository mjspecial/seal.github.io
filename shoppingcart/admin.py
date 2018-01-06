from django.contrib import admin
from models import Student
import models

admin.site.register(models.Student)
admin.site.register(models.Trolley)