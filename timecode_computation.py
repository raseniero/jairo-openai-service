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

# Example usage
time_code = "00:00:23,466 --> 00:00:24,866"

start_time, end_time = extract_start_end_time(time_code)
print("Start Time:", start_time)
print("End Time:", end_time)

frame_rate = 24
start_fractional_frame_rate, offset, duration = convert_to_offset_and_duration(start_time, end_time, frame_rate)
print("Start Time in fractional frame rate format:", start_fractional_frame_rate)
print("Offset in fractional frame rate format:", offset)
print("Duration in fractional frame rate format:", duration)