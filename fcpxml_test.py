import os
import base64
import re


def convert_to_fcpxml(timecode_description, images_base_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(current_dir, 'Template.xml')    
    
    # Load the template.xml content
    with open(template_path, 'r') as file:
        template_content = file.read()
        
    # Replace placeholders in the template with the provided timecode and description
    title_nos = re.findall(r'^(\d+)$', timecode_description, re.MULTILINE)
    timecodes = re.findall(r'(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)', timecode_description)
    descriptions = re.findall(r'<b>(.*?)</b>', timecode_description)
    image_names = re.findall(r'img src="([^"]+)"', timecode_description)


    event_name = 'CC_XML'  # Replace with the desired event name
    project_name = 'FCPX_test/xml2srt'  # Replace with the desired project name

    fcpxml_content = template_content.replace('{EVENT_NAME}', event_name)
    fcpxml_content = fcpxml_content.replace('{PROJECT_NAME}', project_name)


    title_template = '''
        <title name="{TITLE_NO}" offset="{OFFSET}" ref="r2" duration="{DURATION}" start="{START}">
            <param name="Position" key="9999/10199/10201/1/100/101" value="0 -418.279"/>
            <param name="Alignment" key="9999/10199/10201/2/354/1002961760/401" value="1 (Center)"/>
            <param name="Alignment" key="9999/10199/10201/2/373" value="0 (Left) 2 (Bottom)"/>
            <param name="Out Sequencing" key="9999/10199/10201/4/10233/201/202" value="0 (To)"/>
            <param name="Wrap Mode" key="9999/10199/10201/5/10203/21/25/5" value="1 (Repeat)"/>
            <param name="Color" key="9999/10199/10201/5/10203/30/32" value="0 0 0"/>
            <param name="Wrap Mode" key="9999/10199/10201/5/10203/30/34/5" value="1 (Repeat)"/>
            <param name="Width" key="9999/10199/10201/5/10203/30/36" value="3"/>
            <text>
                <text-style ref="ts1">{DESCRIPTION}</text-style>
            </text>
             <image ref="image{TITLE_NO}" offset="0s" duration="{DURATION}" start="{START}" src="{IMAGE_PATH}" />            
            <text-style-def id="ts1">
                <text-style font="Arial" fontSize="50" fontFace="Regular" fontColor="0.999996 1 1 1" shadowColor="0 0 0 0.75" shadowOffset="5 315" alignment="center"/>
            </text-style-def>
        </title>
    '''

    # Initialize the fcpxml_content with template_content
    fcpxml_content = template_content

    spine = ''
    for i, (timecode, description, title_no, image_name) in enumerate(zip(timecodes, descriptions, title_nos, image_names), 1):
        start, end = timecode

         # Convert timecode duration to offset format
        #start = convert_timecode_to_offset(start)  # Convert timecode to offset format
        offset = convert_timecode_to_offset(end)  # Convert timecode to offset format
        duration = convert_timecode_to_offset_duration(start, end)  # Convert timecode duration to offset format
        
        image_path = image_path = os.path.join(images_base_path, image_name)  

        title_content = title_template.format(
            TITLE_NO=title_no,
            OFFSET=offset,
            DURATION=duration,
            START=start,
            DESCRIPTION=description,
            IMAGE_PATH=image_path
        )

        spine += title_content

    fcpxml_content = fcpxml_content.replace('{result}',spine)


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



