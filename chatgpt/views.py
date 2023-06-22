"""
Module to define views for chatgpt
"""
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
import requests
import openai

from .models import ChatGPT
from .serializers import ChatGPTSerializer


# Create your views here.
openai.api_key = "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"
system_prompt = 'I\'m going to paste in a timecode script and I want you to find people, places, things and phrases that you think would help move the story along visually for each timecode spot, write one keyword or phrase and make a list:  \r\n\r\nThe timecode script looks like this:\r\n1 00:00:00,000 --> 00:00:01,800 What would you do if you had  \r\n2 00:00:01,800 --> 00:00:03,433 wandered into a canyon  \r\n3 00:00:03,433 --> 00:00:05,566 known for phantoms that appear  \r\n4 00:00:05,566 --> 00:00:07,866 out of nowhere, dog people that  \r\n5 00:00:07,866 --> 00:00:09,999 fly me to the moon\r\n\r\nOutput should look like this:\r\n1 00:00:01,800: "Decision Making"'
user_prompt = "1 00:00:00,000 --> 00:00:01,800 What would you do if you had  \r\n2 00:00:01,800 --> 00:00:03,433 wandered into a canyon  \r\n3 00:00:03,433 --> 00:00:05,566 known for phantoms that appear  \r\n4 00:00:05,566 --> 00:00:07,866 out of nowhere, dog people that  \r\n5 00:00:07,866 --> 00:00:09,699 supposedly live and hide"


@api_view(["GET"])
def api_root(request, format=None):
    """Function to define api root view"""
    return Response(
        {
            "hello": reverse("hello-world", request=request, format=format),
            "generate keywords": reverse(
                "generate-keywords", request=request, format=format
            ),
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
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},  # get user_prompt from request
        ],
    )

    print(response["choices"][0]["message"]["content"])

    return Response(
        {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "messages": response["choices"][0]["message"]["content"],
        }
    )


class ChatGPTListCreate(generics.ListCreateAPIView):
    """Class to define ChatGPTListCreate view"""

    queryset = ChatGPT.objects.all()
    serializer_class = ChatGPTSerializer


class ChatGPTRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Class to define ChatGPTRetriveUpdateDestroy view"""

    queryset = ChatGPT.objects.all()
    serializer_class = ChatGPTSerializer
