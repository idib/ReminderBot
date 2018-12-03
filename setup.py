TOKEN = ""
REQUEST_KWARGS = {
    # 'proxy_url': 'http://34.216.89.160:8080/'
}
regexpInput = r"(?P<date>(today|tomorrow)|(\d{1,2}([\.\-\/])\d{1,2}(\4(\d{4}|\d{2}))?)|(\d{1,2}([\.\-\/ ]?)(jan|feb|mar|apr|may|juny|july|aug|sept|nov|oct|dec)(\8(\d{4}|\d{2}))?))|(?P<time>\d{1,2}[: ]\d{1,2}|evening|midday|noon|midnight|day|night)|(?P<offset>(\d+[msdhw] ?)+)"
regexpOffset = r"(((?P<weeks>\d+)w|(?P<days>\d+)d|(?P<hours>\d+)h|(?P<minutes>\d+)m|(?P<seconds>\d+)s)[^\w\n]?)+"
setupAPP = {
    'offset': {'hours': 2},
    'midday': {'hour': 12},
    'noon': {'hour': 12},
    'morning': {'hour': 9},
    'evening': {'hour': 21},
    'midnight': {'hour': 00},
    'day': {'hour': 15},
    'night': {'hour': 3}
}
message = {
    'helloWorld': "Hi! Type date, time or duration to set a timer\n example: 10m (10 minutes),\n 5d,\n 3s,\n 5h,\n 2w,\n tomorrow in 17 00,\n tomorrow 17:00,\n evening,\n midday,\n noon,\n midnight\n day,\n night,\n 10m 5d3s5h 2w,\n today,\n tomorrow,\n 17nov,\n 30.11.2019,\n 30 11 2019,\n 30 oct 2019 17:00,\n 30/11/2019,\n 30-11-2019,\n 30 oct 2019 17:00"
}
