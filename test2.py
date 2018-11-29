# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(?P<date>(today|tomorrow)|\d{1,2}([ \.\/]?(jan|feb|mar|apr|may|juny|july|aug|sept|nov|oct|dec)|[ \.\/]\d{1,2})[ \.\/]?(\d{4}|\d{2})?)|(?P<time>\d{1,2}[: ]\d{1,2}|evening|midday|noon|midnight|day|night)|(?P<offset>(\d+[msdhw] ?)+)"

test_str = ("10m\n"
            "5d\n"
            "3s\n"
            "5h\n"
            "2w\n"
            "example: tomorrow,17 00\n"
            "17:00\n\n"
            "evening\n"
            "midday\n"
            "noon\n"
            "midnight\n"
            "day\n"
            "night\n\n"
            "10m 5d3s5h 2w\n\n\n"
            "today\n"
            "tomorrow\n\n"
            "17nov\n"
            "30 oct 2019\n"
            "30.14.2019\n"
            "30/14/2019\n"
            "30 14 2019\n\n"
            "30 oct 2019 17:00\n\n\n"
            "30/14/2019 \n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
