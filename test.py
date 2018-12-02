# from dateutil.parser import parse
# import re
# import datetime
# from setup import *
#
# tests = ["10m", "5d", "3s", "5h", "2w", "example: tomorrow,17 00", "17:00", "evening", "midday", "noon", "midnight",
#          "day", "night", "10m 5d3s5h 2w", "today", "tomorrow", "17nov", "30 oct 2019", "30.11.2019", "30/11/2019",
#          "30 11 2019", "30 oct 2019 17:00", "30/11/2019", "30-11-2019",
#          "30/11/2019 30/14/2019 30 oct 2019 17:00 10m 5d3s5h 2w"]
#
# r = re.compile(regexpInput)
#
# rOffset = re.compile(regexpOffset)
#
#
# def mergeDict(dicts):
#     dict = {'date': None, 'time': None, 'offset': None}
#     result = []
#     i = 0
#     l = len(dicts)
#
#     while i < l:
#         if dicts[i]['date'] and i + 1 < l and dicts[i + 1]['time']:
#             result += [{'date': dicts[i]['date'], 'time': dicts[i + 1]['time'], 'offset': None}]
#             i += 1
#         else:
#             result += [dicts[i]]
#         i += 1
#     return result
#
#
# def offsetConvert(str):
#     m = rOffset.match(str).groupdict()
#     res = {}
#     for k, v in m.items():
#         if k and v:
#             res[k] = int(v)
#     return datetime.timedelta(**res)
#
#
# def formatConversion(dDateTime):
#     res = None
#     today = parse("0:0")
#     now = datetime.datetime.now()
#     strDate = dDateTime['date']
#     strTime = dDateTime['time']
#     strOffset = dDateTime['offset']
#
#     if strOffset:
#         res = {'offset': offsetConvert(strOffset)}
#     elif strDate or strTime:
#         date = None
#         time = None
#         if strDate:
#             strDate = re.sub(r"\.- ", "/", strDate.strip())
#             if strDate == "today":
#                 date = today
#             elif strDate == "tomorrow":
#                 date = today + datetime.timedelta(days=1)
#             else:
#                 date = parse(strDate)
#         if strTime:
#             strTime = strTime.replace(" ", ":")
#             if strTime in setupAPP:
#                 time = today.replace(**setupAPP[strTime])
#             else:
#                 time = parse(strTime)
#         if date and time:
#             res = {'datetime': datetime.datetime.combine(date.date(), time.time())}
#         elif time:
#             if time < now:
#                 time += datetime.timedelta(days=1)
#             res = {'datetime': time}
#         elif date:
#             if date == today:
#                 date += datetime.timedelta(**setupAPP['offset'])
#             else:
#                 date = date.replace(**setupAPP['midday'])
#             if date < today:
#                 date = date.replace(year=date.year + 1)
#             res = {'datetime': date}
#     return res
#
#
# i = 0
# errors = []
# for t in tests:
#     i += 1
#     print("\n\nTEST#" + str(i))
#
#     m = mergeDict([m.groupdict() for m in r.finditer(t)])
#
#     for spls in m:
#         try:
#             structDatetime = formatConversion(spls)
#             print(structDatetime)
#         except:
#             errors += [i]
#             print("we can not convert you message")
#             print(f"we problem exp: {spls}")
#             print(f"original message: {t}")
#
# print()
# print(errors)
