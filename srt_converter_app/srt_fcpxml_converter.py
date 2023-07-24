import os
import base64
import re
import uuid
from datetime import datetime
#from django.core.files.uploadedfile import SimpleUploadedFile

def convert_to_fcpxml(timecode_description, images_directory):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(current_dir, 'Template.xml')    
    
    # Load the template.xml content
    with open(template_path, 'r') as file:
        template_content = file.read()
        
    # Replace placeholders in the template with the provided timecode and description
    title_nos = re.findall(r'^(\d+)$', timecode_description, re.MULTILINE)
    timecodes = re.findall(r'(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)', timecode_description)
    images = re.findall(r'<b>(.*?)</b>', timecode_description)
   


    event_name = 'CC_XML'  # Replace with the desired event name
    project_name = 'FCPX_test/xml2srt'  # Replace with the desired project name

    fcpxml_content = template_content.replace('{EVENT_NAME}', event_name)
    fcpxml_content = fcpxml_content.replace('{PROJECT_NAME}', project_name)


    asset_template = '''
            <asset start="{START}" name="{IMAGE}" id="{TITLE_NO}" duration="{DURATION}" hasVideo="1" format="r3">
                <media-rep kind="original-media" src="{IMAGE_SRC}"/>
            </asset>
    '''

    spine_template = '''
            <video offset="{OFFSET}" start="{START}" name="{IMAGE}" ref="{TITLE_NO}" duration="{DURATION}" enabled="1">
                    <adjust-transform anchor="0 0" position="0 0" scale="1 1"/>
            </video> 
    '''
    # Initialize the fcpxml_content with template_content
    fcpxml_content = template_content

    spine = ''
    asset = ''
    for i, (timecode, title_no, image) in enumerate(zip(timecodes, title_nos, images), 1):
        start, end = timecode

         # Convert timecode duration to offset format
        start = timecode_to_start_offset(start)  # Convert timecode to offset format
        offset = timecode_to_offset(end)  # Convert timecode to offset format
        duration = timecode_to_fractional_seconds_format(start, end)  # Convert timecode duration to offset format
        asset_id = str(uuid.uuid4())  # Generate a unique ID for the asset
        
        image_name = f'{image}'  # Replace with the desired image name
        image_path = os.path.join(images_directory, image_name)  # Construct the image path based on the images directory

        spine_content = spine_template.format(
            TITLE_NO=title_no,
            OFFSET=offset,
            DURATION=duration,
            START=start,
            IMAGE=image_name,
           
        )

        asset_content = asset_template.format(
            TITLE_NO=title_no,
            OFFSET=offset,
            DURATION=duration,
            ASSET_ID=asset_id,
            START=start,
            IMAGE=image_name,
            IMAGE_SRC=image_path
           
        )

        spine += spine_content
        asset += asset_content

    fcpxml_content = fcpxml_content.replace('{spine_result}', spine)
    fcpxml_content = fcpxml_content.replace('{asset_result}', asset )


    # Convert the modified FCPXML content to a base64-encoded string
    fcpxml_bytes = fcpxml_content.encode('utf-8')
    fcpxml_base64 = base64.b64encode(fcpxml_bytes).decode('utf-8')

    return fcpxml_base64


def convert_timecode_to_offset(timecode):
    hours, minutes, seconds, frames = map(int, re.split(r'[:,]', timecode))
    offset_frames = (hours * 60 * 60 * 30) + (minutes * 60 * 30) + (seconds * 30) + frames
    return f'{offset_frames}/30000s'

def convert_timecode_to_offset_duration(start, end):
    start_frames = convert_timecode_to_frames(start)
    end_frames = convert_timecode_to_frames(end)
    duration_frames = end_frames - start_frames
    return f'{duration_frames}/30000s'

def convert_timecode_to_frames(timecode):
    hours, minutes, seconds, frames = map(int, re.split(r'[:,]', timecode))
    total_frames = (hours * 60 * 60 * 30) + (minutes * 60 * 30) + (seconds * 30) + frames
    return total_frames

def timecode_to_offset(timecode):
    start_time, end_time = timecode.split(" --> ")
    start_time = datetime.strptime(start_time, "%H:%M:%S,%f")
    end_time = datetime.strptime(end_time, "%H:%M:%S,%f")

    # Calculate the offset in milliseconds
    offset_ms = (end_time - start_time).total_seconds() * 1000

    # Convert offset to fractional seconds format
    numerator = int(offset_ms)
    denominator = 1000

    # Simplify the fraction if possible
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    divisor = gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor

    return f"{numerator}/{denominator}s"

def timecode_to_fractional_seconds_format(timecode):
    start_time, end_time = timecode.split(" --> ")
    start_time = datetime.strptime(start_time, "%H:%M:%S,%f")
    end_time = datetime.strptime(end_time, "%H:%M:%S,%f")

    # Calculate the duration in microseconds
    duration_microseconds = (end_time - start_time).microseconds

    # Convert duration to fractional seconds format
    numerator = duration_microseconds
    denominator = 1000000

    # Simplify the fraction if possible
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    divisor = gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor

    return f"{numerator}/{denominator}s"


def timecode_to_start_offset(timecode):
    start_time, _ = timecode.split(" --> ")
    start_time = datetime.strptime(start_time, "%H:%M:%S,%f")

    # Convert start time to fractional seconds format
    offset_ms = start_time.microsecond / 1000

    # Convert offset to fractional seconds format
    numerator = int(offset_ms)
    denominator = 1000

    # Simplify the fraction if possible
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    divisor = gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor

    return f"{numerator}/{denominator}s"