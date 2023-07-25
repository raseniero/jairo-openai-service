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
    # Replace placeholders in the template with the provided timecode and description
    timecode_texts = re.split(r'(\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+)\n', timecode_description)
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
    timecodes = timecode_texts[1::2]
    texts = timecode_texts[2::2]
    for i, (timecode, text, title_no, image) in enumerate(zip(timecodes, texts, title_nos, images), 1):
        

         # Convert timecode duration to offset format
        start_time, end_time = extract_start_end_time(timecode)
        frame_rate = 24
        start, offset, duration = convert_to_offset_and_duration(start_time, end_time, frame_rate)   
        

        
         
        asset_id = str(uuid.uuid4())  # Generate a unique ID for the asset
        
        text = text.strip()
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

def convert_to_offset_and_duration(start_time, end_time, frame_rate):
    # Parse the start time and end time to get hours, minutes, seconds, and frames
    start_hours, start_minutes, start_seconds_frames = start_time.split(":")
    start_seconds, start_frames = start_seconds_frames.split(",")
    end_hours, end_minutes, end_seconds_frames = end_time.split(":")
    end_seconds, end_frames = end_seconds_frames.split(",")

    # Calculate the total frames for start time and end time
    start_frames = int(start_frames)
    end_frames = int(end_frames)
    total_start_frames = int(start_hours) * 3600 * frame_rate + int(start_minutes) * 60 * frame_rate + int(start_seconds) * frame_rate + start_frames
    total_end_frames = int(end_hours) * 3600 * frame_rate + int(end_minutes) * 60 * frame_rate + int(end_seconds) * frame_rate + end_frames

    # Calculate the offset as the total frames of the start time
    offset_frames = total_start_frames

    # Calculate the duration in frames by subtracting total frames of the start time from total frames of the end time
    duration_frames = total_end_frames - total_start_frames

    # Format the start time, offset, and duration into the fractional frame rate format
    start_fractional_frame_rate = f'{offset_frames}/{frame_rate}s'
    offset = f'{offset_frames}/{frame_rate}s'
    duration = f'{duration_frames}/{frame_rate}s'

    return start_fractional_frame_rate, offset, duration

def extract_start_end_time(time_code):
    start_time_str, end_time_str = time_code.split(" --> ")

    # Extract start time components (hours, minutes, seconds, and frames)
    start_hours, start_minutes, start_seconds_frames = start_time_str.split(":")
    start_seconds, start_frames = start_seconds_frames.split(",")
    start_time = f'{int(start_hours):02d}:{int(start_minutes):02d}:{int(start_seconds):02d},{start_frames}'

    # Extract end time components (hours, minutes, seconds, and frames)
    end_hours, end_minutes, end_seconds_frames = end_time_str.split(":")
    end_seconds, end_frames = end_seconds_frames.split(",")
    end_time = f'{int(end_hours):02d}:{int(end_minutes):02d}:{int(end_seconds):02d},{end_frames}'

    return start_time, end_time



