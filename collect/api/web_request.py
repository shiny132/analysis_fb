from urllib.request import  Request,urlopen
from datetime import *
import sys
import json
# def result_print(json_result):
#     print("a")

def json_request(
    url = ' ',
    encoding = 'utf-8',
    success = None,
    error = lambda e : print('%s %s' % (e, datetime.now()), file=sys.stderr)  # standard err
    ):  # 함수 한줄로 만들기
    # success = function(함수명)
    try:
        request = Request(url) # request객체 생성
        resp = urlopen(request) # 응답 받기
        resp_body = resp.read().decode(encoding) # 응답 읽기 (바디 내용)  - 바이트로 통신    인코딩 했으면 디코딩도 해야함
        json_result = json.loads(resp_body) # 읽어온 url의 바디(코드)를 가져옴 - json형태(딕셔너리)로 불러옴
        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:  # 함수인지 아닌지를 판별
            return json_result  # return값을 주는 의미는 바깥에서 처리해라 뜻

        success(json_result)

    except Exception as e:
        if callable(error) is True:
            error(e)


def html_request(
        url=' ',
        encoding = 'utf-8',
        success = None,
        error = lambda e : print('%s %s' % (e,datetime.now()),file = sys.stderr) #standard err
        ):# 함수 한줄로 만들기
# success = function(함수명)
    try:
        Request(url)  # request객체 생성
        request = Request(url)
        resp = urlopen(request)

    # 응답내용을 다 읽는다.
        html = resp.read().decode(encoding)

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False: # 함수인지 아닌지를 판별
            return html # return값을 주는 의미는 바깥에서 처리해라 뜻

        success(html)

    except Exception as e:
         if callable(error) is True:
             error(e)



# qq = json_request('http://kickscar.cafe24.com:8080/myapp-api/api/user/list')
# print(qq)