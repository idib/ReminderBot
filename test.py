from dateutil.parser import parse
import re
import datetime
from setup import *

tests = ["10m", "5d", "3s", "5h", "2w", "example: tomorrow,17 00", "17:00", "evening", "midday", "noon", "midnight",
         "day", "night", "10m 5d3s5h 2w", "today", "tomorrow", "17nov", "30 oct 2019", "30.11.2019", "30/11/2019",
         "30 11 2019", "30 oct 2019 17:00", "30/11/2019", "30-11-2019",
         "30/11/2019 30/14/2019 30 oct 2019 17:00 10m 5d3s5h 2w"]

r = re.compile(regexpInput)

rOffset = re.compile(regexpOffset)


def mergeDict(dicts):
    dict = {'date': None, 'time': None, 'offset': None}
    result = []
    i = 0
    l = len(dicts)

    while i < l:
        if dicts[i]['date'] and i + 1 < l and dicts[i + 1]['time']:
            result += [{'date': dicts[i]['date'], 'time': dicts[i + 1]['time'], 'offset': None}]
            i += 1
        else:
            result += [dicts[i]]
        i += 1
    return result


def offsetConvert(str):
    m = rOffset.match("10m 5d3s5h 2w").groupdict()
    m = {k: int(v) for k, v in m.items()}
    return datetime.timedelta(**m)


def formatConversion(dicts):
    for dict in dicts:
        today = datetime.datetime.today()
        date = None
        time = None
        offset = None
        if not dict["date"] or dict["date"] == "today":
            offset = offsetConvert(setupAPP['defaultOffset'])
        elif dict["date"] == "tomorrow":
            date = today + datetime.timedelta(days=1)
        else:
            parse(dict["date"])

        date.replace()


    return


i = 0
for t in tests:
    i += 1
    print("\n\nTEST#" + str(i))

    m = [m.groupdict() for m in r.finditer(t)]

    m = mergeDict(m)
    listDate = formatConversion(m)

    for d in m:
        if d["date"] or d["time"]:
            strDateTime = (d["date"] if d["date"] else "") + " " + (d["time"] if d["time"] else "1200")
            try:
                print("date: {}".format(parse(strDateTime)), end=' ')
            except ValueError:
                print("except")
                print("date: {}".format(strDateTime, end=' '))

        if d["offset"]:
            print("offset: {}".format(d["offset"]), end=' ')
        print()
    # print(m)
#
#
# test2 = "30/14/2019 30/14/2019 30 oct 2019 17:00 10m 5d3s5h 2w"
# m = [m.groupdict() for m in r.finditer(test2)]
# print(m)
# print('\n\n\n\n')
# mergeDict(m)
