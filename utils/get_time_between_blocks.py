import json

def get_time_between_blocks(blocks_file_path):
    """
    Return the time between blocks in a file.
    """
    timestamps = []
    with open(blocks_file_path) as blocks_file:
        for line in blocks_file:
            block = json.loads(line)
            time = block['time']
            timestamps.append(time)

    timestamps_diff = []

    for index, timestamp in enumerate(timestamps):
        if index > 0:
            previous_timestamp = timestamps[index - 1]
            time_diff = previous_timestamp - timestamp
            timestamps_diff.append(time_diff)

    return timestamps_diff
