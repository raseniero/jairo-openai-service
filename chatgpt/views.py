"""
Module to define views for chatgpt
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from .models import ChatGPT
from .serializers import ChatGPTSerializer


# Create your views here.
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "chatgpts": reverse("chatgpt-list", request=request, format=format),
        }
    )


class ChatGPTListCreate(generics.ListCreateAPIView):
    queryset = ChatGPT.objects.all()
    serializer_class = ChatGPTSerializer


class ChatGPTRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatGPT.objects.all()
    serializer_class = ChatGPTSerializer
