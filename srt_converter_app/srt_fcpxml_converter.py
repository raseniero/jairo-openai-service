import os
import base64
import re
import uuid
from fractions import Fraction

def convert_to_fcpxml(timecode_description, images_directory):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(current_dir, 'Template.xml')    
    
    # Load the template.xml content
    with open(template_path, 'r') as file:
        template_content = file.read()
        
    # Replace placeholders in the template with the provided timecode and description
    position_nos = re.findall(r'^(\d+)$', timecode_description, re.MULTILINE)
    # Replace placeholders in the template with the provided timecode and description
    timecode_texts = re.split(r'(\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+)\n', timecode_description)
    images = re.findall(r'<b>(.*?)</b>', timecode_description)

    event_name = 'CC_XML'  # Replace with the desired event name
    project_name = 'FCPX_test/xml2srt'  # Replace with the desired project name

    fcpxml_content = template_content.replace('{EVENT_NAME}', event_name)
    fcpxml_content = fcpxml_content.replace('{PROJECT_NAME}', project_name)

    asset_template = '''
            <asset start="0/1s" name="{IMAGE}" id="{POSITION_NO}" duration="0/1s" hasVideo="1" format="r3">
                <media-rep kind="original-media" src="{IMAGE_SRC}"/>
            </asset>
    '''

    spine_template = '''
            <video offset="{OFFSET}" start="0/1s" name="{IMAGE}" ref="{POSITION_NO}" duration="{DURATION}" enabled="1">
                    <adjust-transform anchor="0 0" position="0 0" scale="1 1"/>
            </video> 
    '''

    spine = ''
    asset = ''
    timecodes = timecode_texts[1::2]
    texts = timecode_texts[2::2]
    for i, (timecode, text, position_no, image) in enumerate(zip(timecodes, texts, position_nos, images), 1):
        # Convert timecode duration to offset format
        frame_rate = 30  # Replace with the desired frame rate
        #offset, duration = timecode_to_framerate(timecode, frame_rate)
        #offsets = f"{offset.numerator}/{offset.denominator}s"
        #durations = f"{duration.numerator}/{duration.denominator}s"
        offset, duration = timecode_to_fcpxml(timecode, frame_rate)
        offsets = f"{offset.numerator}/{offset.denominator}s"
        durations = f"{duration.numerator}/{duration.denominator}s"
        
        
        
        asset_id = str(uuid.uuid4())  # Generate a unique ID for the asset
        
        text = text.strip()
        image_name = f'{image}'  # Replace with the desired image name
        image_path = os.path.join(images_directory, image_name)  # Construct the image path based on the images directory

        spine_content = spine_template.format(
            POSITION_NO=position_no,
            OFFSET=offsets,
            DURATION=durations,
            IMAGE=image_name,
        )

        asset_content = asset_template.format(
            POSITION_NO=position_no,
            OFFSET=offsets,
            DURATION=durations,
            ASSET_ID=asset_id,
            IMAGE=image_name,
            IMAGE_SRC=image_path
        )

        spine += spine_content
        asset += asset_content

    fcpxml_content = fcpxml_content.replace('{spine_result}', spine)
    fcpxml_content = fcpxml_content.replace('{asset_result}', asset)

    # Convert the modified FCPXML content to a base64-encoded string
    fcpxml_bytes = fcpxml_content.encode('utf-8')
    fcpxml_base64 = base64.b64encode(fcpxml_bytes).decode('utf-8')

    return fcpxml_base64


def timecode_to_framerate(timecode_str, framerate):
    # Parse the timecode string into offset and duration
    offset_str, duration_str = timecode_str.strip().split(" --> ")
    offset_h, offset_m, offset_s_ms = offset_str.split(":")
    duration_h, duration_m, duration_s_ms = duration_str.split(":")
    offset_s, offset_ms = offset_s_ms.split(",")
    duration_s, duration_ms = duration_s_ms.split(",")

    # Convert offset and duration to seconds
    offset_seconds = int(offset_h) * 3600 + int(offset_m) * 60 + int(offset_s) + int(offset_ms) / 1000.0
    duration_seconds = int(duration_h) * 3600 + int(duration_m) * 60 + int(duration_s) + int(duration_ms) / 1000.0

    # Calculate fractional offset and duration
    offset_fraction = Fraction(round(offset_seconds * framerate), framerate)
    duration_fraction = Fraction(round(duration_seconds * framerate), framerate)

    return offset_fraction, duration_fraction


def timecode_to_fcpxml(timecode_str, framerate):
    offset_str, duration_str = timecode_str.split(" --> ")
    offset, duration = offset_str.strip(), duration_str.strip()

    # Function to convert timecode string to fractional frame format
    def to_fractional_frame(timecode):
        h, m, s_ms = timecode.split(":")
        s, ms = s_ms.split(",")
        total_seconds = int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0
        return Fraction(round(total_seconds * framerate), framerate)

    offset_fraction = to_fractional_frame(offset)
    duration_fraction = to_fractional_frame(duration)

    offset_str = f"{offset_fraction.numerator}/{offset_fraction.denominator}s"
    duration_str = f"{duration_fraction.numerator}/{duration_fraction.denominator}s"

    return offset_fraction, duration_fraction