from django.contrib import admin
from .models import Student, TimeLine
from .models import Professor
# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(TimeLine)