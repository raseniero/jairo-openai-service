from fractions import Fraction


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

# Example usage with 30 frames per second (fps) frame rate
timecode_str = "01:00:00,033 --> 01:00:03,400"
framerate = 30

offset, duration = timecode_to_framerate(timecode_str, framerate)
print("Offset:", f"{offset.numerator}/{offset.denominator}s")
print("Duration:", f"{duration.numerator}/{duration.denominator}s")