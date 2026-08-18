from django.contrib import admin
from Core.models import User, Classroom, Grade, Student, Subject 
# Register your models here.
admin.site.register(User)
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Grade)