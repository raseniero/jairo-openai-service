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
from bs4 import BeautifulSoup
from rest_framework.views import APIView


from django.http import JsonResponse

from jairo_openai_service import settings

from .models import ChatGPT
from .serializers import ChatGPTSerializer



api_key_1 = settings.API_KEYS[0]
api_key_2 = settings.API_KEYS[1]


# Create your views here.
# You have the options to use other API key or the secret key
openai.api_key = api_key_1
openai.api_key = api_key_2





@api_view(["GET"])
def api_root(request, format=None, pk=1):
    
    """Function to define api root view"""
    return Response(
        {
            "hello": reverse("hello-world", request=request, format=format),
            "generate keywords": reverse(
                "generate-keywords", request=request, format=format
            ),
            "generate images": reverse(
                "generate-image", request=request, format=format
            ),
                        "scrape google images": reverse(
                "scrape-google-images", request=request, format=format
            )

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


@api_view(["POST"])
def generate_keywords(request):
 
    # Retrieve the user_prompt from the request data
    user_prompt = request.data.get('user_prompt')

    # Define the system_prompt
    system_prompt = "I'm going to paste in a timecode script and I want you to find people, places, things and phrases that you think would help move the story along visually for each timecode spot, write one keyword or phrase and make a list:  \r\n\r\nThe timecode script looks like this:\r\n1 00:00:00,000 --> 00:00:01,800 What would you do if you had  \r\n2 00:00:01,800 --> 00:00:03,433 wandered into a canyon  \r\n3 00:00:03,433 --> 00:00:05,566 known for phantoms that appear  \r\n4 00:00:05,566 --> 00:00:07,866 out of nowhere, dog people that  \r\n5 00:00:07,866 --> 00:00:09,999 fly me to the moon\r\n\r\nOutput should look like this:\r\n1 00:00:01,800: \"Canyon Exploration\",\r\n2 00:00:01,800: \"Lost in Canyon\",\r\n3   00:00:01,800: \"Mysterious Phantoms\",\r\n4 00:00:01,800: \"Mythical Dog People\",\r\n5 00:00:01,800: \"Decision Making\", "
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



class ImageGenerationView(APIView):
    def post(self, request):
            prompt = request.data.get('prompt', '')

            response = openai.Image.create(
                prompt=prompt,
                n = 1,
                size= "1024x1024"
            )
            image_url = response["data"][0]["url"]
            #image_url = [data['url'] for data in response['data']]
            #image_url = [choice['text'].strip() for choice in response.choices]
            return Response({'image_url': image_url})


class ChatGPTListCreate(generics.ListCreateAPIView):
    """Class to define ChatGPTListCreate view"""

    queryset = ChatGPT.objects.all()
    serializer_class = ChatGPTSerializer


class ChatGPTRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Class to define ChatGPTRetriveUpdateDestroy view"""

    queryset = ChatGPT.objects.all()
    serializer_class = ChatGPTSerializer


@api_view(['POST'])
def scrape_google_images(request):
    # Get the search query from the request parameters
    query = request.data.get('query')
    
    # Prepare the URL for the Google Images search
    search_url = f'https://www.google.com/search?q={query}&source=lnms&tbm=isch'
    
    # Send a GET request to the search URL
    response = requests.get(search_url)
    
    # Parse the response HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the image elements on the page
    images = soup.find_all('img')
    
    # Extract the image URLs
    image_urls = [{'url': img['src']} for img in images]
    
    # Return the image URLs as a JSON response
    return Response({'images': image_urls})




