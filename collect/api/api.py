# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN = "EAACEdEose0cBABiPRdJ1Vngjs5UwoYjEwy5d22f23W4KwPSjGiKWEClcdMcK82Qd0vjmYfp5ATAuMEHGMQTZB6gKjJZBjsIknZAvZC1lZAXZAg2skGE1EUvWMQjstOIs2V4gZA43KJ1JtW7ienFf3cabZB985D2IfoW38Lg39IxgAoXBQNPQDCYOZBcBnLuokj946B0zkFm8w7AZDZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"

def fb_gen_url(
    base = BASE_URL_FB_API,
    node='',
    **params):
    url = '%s/%s/?%s' % (base, node, urlencode(params))
    return url

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")

def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(node=fb_name_to_id(pagename)+"/posts/",
        fields= 'id, message, link, name, type, shares, reactions, created_time, comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit= 50,
        access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    print(json_result)
