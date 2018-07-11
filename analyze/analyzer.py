import json
import re
from konlpy.tag import Twitter
from collections import Counter

def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')
    json_string = jsonfile.read()
    jsonfile.close()
    # print(json_string)
    data = ''
    json_data = json.loads(json_string)
    for item in json_data:
        value = item.get(key)
        if value is None:
            continue
        data += re.sub(r'[^\w]', '', value)
        # print(value)
    return data


def count_wordfreq(data):
    twitter = Twitter()
    nouns = twitter.nouns(data)
    # print(nouns)
    count = Counter(nouns)
    return count