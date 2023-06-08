from django.contrib import admin
from .models import ChatGPT  # Import the ChatGPT model from chatgpt/models.py

# Register your models here.
admin.site.register(ChatGPT)  # Register the ChatGPT model with the admin site
