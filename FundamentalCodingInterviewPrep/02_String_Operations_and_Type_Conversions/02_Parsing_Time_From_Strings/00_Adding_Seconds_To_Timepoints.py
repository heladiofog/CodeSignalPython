# You are given two input arguments: an array of strings `timePoints` and an integer `added_seconds`. Each string in `timePoints` is in the `HH:MM:SS` format, representing a valid time from `"00:00:00"` to `"23:59:59"` inclusive. The integer `added_seconds` represents a number of seconds, ranging from 1 to 86,400. Your task is to create a new function, `add_seconds_to_times(timePoints, added_seconds)`, which takes these two arguments and returns a new array of strings. Each string in the returned array is the new time, calculated by adding the provided `added_seconds` to the corresponding time in `timePoints`, formatted in `HH:MM:SS`.

# The array `timePoints` contains `n` strings, where n can be any integer from 1 to 100 inclusive. The time represented by each string in `timePoints` is guaranteed to be valid. The total time, after adding `added_seconds`, can roll over to the next day.

# Example

# For timePoints = ['10:00:00', '23:30:00'] and added_seconds = 3600, the output should be ['11:00:00', '00:30:00'].

def add_seconds_to_times(timePoints, seconds):
  # TODO: implement the function
  pass

# Solution:
def add_seconds_to_times(timePoints, seconds):
  # TODO: implement the function
    final_time_points = []
    added_seconds = seconds # var name confussion
    
    for time_point in timePoints:
        time_parts = [int(part) for part in time_point.split(":")]
        # print(f"time to process:{time_point}, time parts: {time_parts}")
        initial_seconds = time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
        total_seconds = (initial_seconds + added_seconds) % (24 * 3600)
        # print(f"adding {seconds}, initial seconds-final seconds: {initial_seconds}-{total_seconds}")
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        final_time_points.append(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        # final_time_points.append(add_seconds_to_timepoint(time_point, seconds))
    
    print(f"Final Timepoints: {final_time_points}")
    return final_time_points
    pass
    
def add_seconds_to_timepoint(time_point, seconds):
    time_parts = [int(part) for part in time_point.split(":")]
    initial_seconds = time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
    total_seconds = (initial_seconds + seconds) % (24 * 3600)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
