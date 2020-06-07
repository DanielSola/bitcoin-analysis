import json
from datetime import datetime


def get_avg_block_size_by_hour(blocks_file_path):
    """
    Return the sum of block sizes for a given hour in a given date in file.
    Dictionary keys is date and hour, and value is block size
    Ex: { '2020-06-01 16': 1340285 }
    """

    blocks_by_date_hour = {}

    with open(blocks_file_path) as blocks_file:
        for line in blocks_file:
            block = json.loads(line)
            timestamp = block['time']
            date_hour_format = '%Y-%m-%d %H'
            block_time = datetime.fromtimestamp(timestamp).strftime(date_hour_format)
            block_size = block['size']

            if block_time in blocks_by_date_hour:
                blocks_by_date_hour[block_time].append(block_size)
            else:
                blocks_by_date_hour[block_time] = [block_size]

    block_size_by_date_hour = {}

    for date_hour in blocks_by_date_hour:
        blocks_in_hour = blocks_by_date_hour[date_hour]
        block_size_by_date_hour[date_hour] = sum(blocks_in_hour) / len(blocks_in_hour)

    return block_size_by_date_hour
