from fractions import Fraction

#edit
def timecode_to_framerate(timecode_str, framerate):
    # Parse the timecode string into offset and duration
    offset_str, duration_str = timecode_str.strip().split(" --> ")
    offset_h, offset_m, offset_s_ms = offset_str.split(":")
    duration_h, duration_m, duration_s_ms = duration_str.split(":")
    offset_s, offset_ms = offset_s_ms.split(",")
    duration_s, duration_ms = duration_s_ms.split(",")

    # Convert offset and duration to seconds
    offset_seconds = int(offset_h) * 3600 + int(offset_m) * 60  + int(offset_s) + int(offset_ms) / 1000.00
    duration_seconds = int(duration_h) * 3600 + int(duration_m) * 60 + int(duration_s) + int(duration_ms) / 1000.0
    print(offset_seconds)
    print(duration_seconds)
    
    # Calculate fractional offset and duration
    offset_fraction = offset_seconds * framerate
    offsets = round(offset_fraction)
    print(f"{offsets}/24")
    
    
    duration_fraction = duration_seconds - offset_seconds 
    duration = duration_fraction * 24
    durations = round(duration)
    print(f"{durations}/24")

    return durations, duration_fraction

# Example usage with 30 frames per second (fps) frame rate
timecode_str = "01:00:03,400 --> 01:00:04,733"
framerate = 24

offset, duration = timecode_to_framerate(timecode_str, framerate)


