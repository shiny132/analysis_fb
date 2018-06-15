# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN = "EAACEdEose0cBAI3ZCoKuOR4vvof9fzOevq2nCQ1QjvUNY65JPbDx6l4SG6QnsiuLz1fbQWUidlEsVlWQ39Bt816ddl1ZAiXrfRiHrYZAdgFxrsXlXQajEO2IrZCEHIoZBicQhbgNxZC3aYa3JWX0Q8d5HTpDoAeWXj28sr4TXiA8U4alsZCNsavuvNfZAobHZClTlmS8FwHVHCgZDZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"

def fb_gen_url(
    base = BASE_URL_FB_API,
    node='',
    **params):
    url = '%s/%s/?%s' % (base, node, urlencode(params))
    print(url)
    return url

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(node=fb_name_to_id(pagename) + "/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since,
                     until=until,
                     limit=50,
                     access_token=ACCESS_TOKEN)

    # results = [] # yield로 대체
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)
        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')
        # results += posts
        # results.append(posts)
        url = None if paging is None else paging.get("next")
        isnext = url is not None
        
        yield posts

    # return results # while문 안에 yield로 대체

        # if url is not None:  # 이코드가 위의 url 삼항연산자로 대체됨
        #     isnext = True
        # else:
        #     isnext = False

        # if json_result is None:  # 이 코드가 위의 paging 삼항연산자로 대체됨
        #     paging = None
        # else:
        #     paging = json_result
