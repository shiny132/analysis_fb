# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN = "EAACEdEose0cBAC9ZCkLaEG608EOpA0ZC8WlmTNbF0YtkJt6aFWhJRS3JthHc06wwy7Vdyk3fvUPQ401G7L8cN6ccCA5EZBpQduHkAQIYvESNCLuwlZApRD1qjJ7NueTn78KDxXYdegIyExHrczGftMZA1vuq5HC886Cj2KDsUXpG4prKMblrmcZCMIsZA2QaM14n46MFZAh9MAZDZD"
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