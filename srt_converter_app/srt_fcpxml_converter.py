import os
import base64
import re
import uuid
#from django.core.files.uploadedfile import SimpleUploadedFile

def convert_to_fcpxml(timecode_description):
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
                <media-rep kind="original-media" src="C:/Users/User/Downloads/{IMAGE}"/>
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
    for i, (timecode, image, title_no) in enumerate(zip(timecodes, images, title_nos), 1):
        start, end = timecode

         # Convert timecode duration to offset format
        #start = convert_timecode_to_offset(start)  # Convert timecode to offset format
        offset = convert_timecode_to_offset(end)  # Convert timecode to offset format
        duration = convert_timecode_to_offset_duration(start, end)  # Convert timecode duration to offset format
        asset_id = str(uuid.uuid4())  # Generate a unique ID for the asset

        spine_content = spine_template.format(
            TITLE_NO=title_no,
            OFFSET=offset,
            DURATION=duration,
            START=start,
            IMAGE=image,
           
        )

        asset_content = asset_template.format(
            TITLE_NO=title_no,
            OFFSET=offset,
            DURATION=duration,
            ASSET_ID=asset_id,
            START=start,
            IMAGE=image,
           
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



