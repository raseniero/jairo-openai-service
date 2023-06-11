from django.contrib import admin
from .models import ChatGPT  # Import the ChatGPT model from chatgpt/models.py
from .models import ApplicationSettings

# Register your models here.
admin.site.register(ChatGPT)
admin.site.register(ApplicationSettings)
