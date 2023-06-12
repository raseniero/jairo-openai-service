"""
Module to define views for chatgpt
"""
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
import requests

from .models import ChatGPT
from .serializers import ChatGPTSerializer


# Create your views here.
@api_view(["GET"])
def api_root(request, format=None):
    """Function to define api root view"""
    return Response(
        {
            "chatgpts": reverse("chatgpt-list", request=request, format=format),
            "hello": reverse("hello-world", request=request, format=format),
            "keywords": reverse("generate-keywords", request=request, format=format),
        }
    )


@api_view(["GET"])
def hello_world(request):
    """Function to define hello world view"""
    return Response(
        {
            "message": "Hello World! Now is "
            + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }
    )


@api_view(["GET"])
def generate_keywords(request):
    """Function to define generate keywords view"""
    response = requests.get("https://www.thunderclient.com/welcome")
    print("response.text=" + response.text)
    return Response(response.text)


class ChatGPTListCreate(generics.ListCreateAPIView):
    """Class to define ChatGPTListCreate view"""

    queryset = ChatGPT.objects.all()
    serializer_class = ChatGPTSerializer


class ChatGPTRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Class to define ChatGPTRetriveUpdateDestroy view"""

    queryset = ChatGPT.objects.all()
    serializer_class = ChatGPTSerializer
