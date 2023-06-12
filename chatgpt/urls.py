"""
Module to define the chatgpt urls
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("chatgpts/", views.ChatGPTListCreate.as_view(), name="chatgpt-list"),
    path(
        "chatgpt/<int:pk>/",
        views.ChatGPTRetriveUpdateDestroy.as_view(),
        name="chatgpt-detail",
    ),
    path("hello/", views.hello_world, name="hello-world"),
    path("keywords/", views.generate_keywords, name="generate-keywords"),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
