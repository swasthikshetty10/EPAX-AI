from django.contrib import admin

# Register your models here.
from .models import UserNotes, Todo, feedback

admin.site.register(UserNotes)
admin.site.register(Todo)
admin.site.register(feedback)
