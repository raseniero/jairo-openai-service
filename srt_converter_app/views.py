from rest_framework.decorators import api_view
from rest_framework.response import Response
from .srt_converter import convert_to_fcpxml

@api_view(['POST'])
def convert_text_to_fcpxml(request):
    text = request.data.get('text', '')

    try:
        fcpxml = convert_to_fcpxml(text)
        return Response(fcpxml)
    except Exception as e:
        return Response({'error': str(e)}, status=400)