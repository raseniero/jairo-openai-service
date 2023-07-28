def offset_duration_to_timecode(offset, start, duration, frame_rate=24):
    # Convert offset to milliseconds
    offset_ms, _ = map(int, offset[:-2].split('/'))

    # Convert start to frames
    start_frames, start_denominator = map(int, start[:-1].split('/'))

    # Convert duration to frames
    duration_frames, duration_denominator = map(int, duration[:-1].split('/'))

    # Calculate the total milliseconds for the start timecode
    total_start_ms = offset_ms + (start_frames * 1000 / (frame_rate / start_denominator))

    # Calculate the total milliseconds for the end timecode
    total_end_ms = total_start_ms + (duration_frames * 1000 / (frame_rate / duration_denominator))

    # Calculate hours, minutes, seconds, and milliseconds for start and end timecodes
    h_start, total_start_ms = divmod(total_start_ms, 3600000)
    m_start, total_start_ms = divmod(total_start_ms, 60000)
    s_start, ms_start = divmod(total_start_ms, 1000)

    h_end, total_end_ms = divmod(total_end_ms, 3600000)
    m_end, total_end_ms = divmod(total_end_ms, 60000)
    s_end, ms_end = divmod(total_end_ms, 1000)

    # Format the timecode strings
    start_timecode = "{:02d}:{:02d}:{:02d},{:03d}".format(int(h_start), int(m_start), int(s_start), int(ms_start))
    end_timecode = "{:02d}:{:02d}:{:02d},{:03d}".format(int(h_end), int(m_end), int(s_end), int(ms_end))

    return f"{start_timecode} --> {end_timecode}"


# Example usage with the provided offset, start, and duration values
offset = "54001/15s"
start = "0/1s"
duration = "61/30s"
frame_rate = 30

# Convert back to timecode range
timecode_range = offset_duration_to_timecode(offset, start, duration, frame_rate)
print(timecode_range)

def timecode_to_offset_start_duration(timecode_range, frame_rate=24):
    def timecode_to_ms(timecode):
        h, m, s_ms = timecode.split(':')
        s, ms = s_ms.split(',')
        total_ms = int(h) * 3600000 + int(m) * 60000 + int(s) * 1000 + int(ms)
        return total_ms

    # Split the timecode range into start and end timecodes
    start_timecode, end_timecode = timecode_range.split(" --> ")

    # Convert the timecodes to milliseconds
    total_start_ms = timecode_to_ms(start_timecode)
    total_end_ms = timecode_to_ms(end_timecode)

    # Calculate the offset in milliseconds
    offset_ms = total_start_ms

    # Calculate the start and duration in frames
    start_frames = (total_start_ms / 1000) * frame_rate
    duration_frames = ((total_end_ms - total_start_ms) / 1000) * frame_rate

    # Convert the start and duration frames to fractions
    start_numerator = int(start_frames)
    start_denominator = frame_rate
    duration_numerator = int(duration_frames)
    duration_denominator = frame_rate

    # Format the offset, start, and duration strings
    offset = f"{offset_ms}/{1000}ms"
    start = f"{start_numerator}/{start_denominator}s"
    duration = f"{duration_numerator}/{duration_denominator}s"

    return offset, start, duration


# Example usage to convert the timecode back to offset, start, and duration
timecode_range = "01:00:00,033 --> 01:00:03,400"
frame_rate = 30

# Convert timecode range to offset, start, and duration
offset, start, duration = timecode_to_offset_start_duration(timecode_range, frame_rate)

print("Offset:", offset)
print("Start:", start)
print("Duration:", duration)