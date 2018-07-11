#from analysis_fb.collect import crawler as cw
#from collect import crawler as cw   # cmd에서 출력할 때
from analyze import analyzer as analyze
import collect
from config import CONFIG
import visualize
# import analyze
# import visualize

if __name__ == '__main__':
    for pagename in CONFIG['pagename']:
        collect.crawling(pagename,
        **CONFIG['common'])

    # items = [
    #     {'pagename' : 'jtbcnews', 'since' : '2017-01-01', 'until' : '2017-12-31'},
    #     {'pagename' : 'chosun', 'since' : '2017-01-01', 'until' : '2017-12-31'}
    # ]

    # 데이터 수집(collection)
    # for item in items:
    #     collect.crawling(**item)

    # collect.crawling(
    #     "jtbcnews",
    #     '2017-01-01',
    #     '2017-12-31')

    # 데이터 분석(analyze)

    # 데이터 시각화(visualize)

#if __name__ == '__main__':
#    cw.crawling("jtbcnews", '2017-01-01', '2017-12-31')

# cw.crawling("jtbcnews", '2017-01-01', '2017-12-31')

# # version3
#     # 데이터 수집
#     for item in items:
#         resultfile = collect.crawling(**item, fetch=False)
#         item['resultfile'] = resultfile
#
#     # 데이터 분석
#     # for item in items:
#     #     print(item['resultfile'])
#     for item in items:
#         print(item)
#         data = analyze.json_to_str(item['resultfile'], 'message')
#         item['count_wordfreq'] = analyze.count_wordfreq(data)
#         # print(data)
#         print(item['count_wordfreq'])
#
# # 데이터 시각화(visualize)
#     for item in items:
#         count = item['count_wordfreq']
#         count_m50 = dict(count.most_common(50))
#         filename = "%s_%s_%s" % (item['pagename'], item['since'], item['until'])
#         visualize.wordcloud(filename,count_m50)
#         # visualize.graph_bar()
#         # print(count_m50)