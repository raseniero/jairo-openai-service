from rest_framework.decorators import api_view
from rest_framework.response import Response
from .srt_fcpxml_converter import convert_to_fcpxml
import os

@api_view(['POST'])
def convert_text_to_fcpxml(request):
    text = request.data.get('text', '')
    images_directory = os.getcwd() # Get the current working directory
    

    try:
        fcpxml_json = convert_to_fcpxml(text, images_directory)
        return Response({'fcpxml': fcpxml_json})
    except Exception as e:
        return Response({'error': str(e)}, status=400)