from rest_framework.decorators import api_view
from rest_framework.response import Response
from .srt_converter import convert_to_fcpxml
import json
from django.http import JsonResponse

@api_view(['POST'])
def convert_text_to_fcpxml(request):
    text = request.data.get('text', '')
    json_data = json.dumps({"text": text})
    
   
    

    try:
        fcpxml_json = convert_to_fcpxml(json_data)
        return Response({'fcpxml': fcpxml_json})
    except Exception as e:
        return Response({'error': str(e)}, status=400)