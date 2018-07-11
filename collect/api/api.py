# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

# ACCESS_TOKEN = "EAACEdEose0cBAA0SM5nfCvGsieIhPoUAkIpNjvrZBuZBs0eIsQI8uBefBdpIes2HQCgYUacGiuDppgTIJRmZBYwuvlq9niMrRv8ZAPMZAKJF6ugewsrcOnpD09SKNCOjMPlfiyuQWkmjN2bcBkRpTtvYNiEdVQzMVauWQdPSDSsQVrtf4Iod6PNfY8RbJdOwZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"

def fb_gen_url(
    base = BASE_URL_FB_API,
    node='',
    **params):
    url = '%s/%s/?%s' % (base, node, urlencode(params))
    print(url)
    return url

def fb_name_to_id(pagename, access_token):
    url = fb_gen_url(node=pagename, access_token=access_token)
    json_result = json_request(url=url)
    return json_result.get("id")


def fb_fetch_posts(pagename, since, until, access_token=''):
    url = fb_gen_url(
        node=fb_name_to_id(pagename, access_token)+"/posts",
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=access_token)

    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

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
