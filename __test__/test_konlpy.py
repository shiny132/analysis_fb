from konlpy.tag import Kkma

kkma = Kkma()

sentences = kkma.sentences(u'네, 안녕하세요. 반갑습니다.')
print(sentences)

nouns = kkma.nouns(u'오늘(12일)의 한마디는 이젠 MB가 답할 때입니다. 세금 안 내려고 위장 이혼까지? 고액 체납자 수색 현장! 집안 곳곳에 가지각색 금품이...41명 살 썩게 만든 감기 주사, 유효 기간도 모르고 사용? 부끄러운 줄 알아야지! 지난 90년대 율곡사업 비리와 같은 엄청난 사건은 물론이고, 2000년대 이후9건에 달하는 굵직굵직했던 방산비리 사건에 대해 환수를 위한 민사 소송을 진행한 것은 0건. 관련 부처들은 비리가 드러났어도 천문학적인 세금이 공중으로 날아갔어도 별다른 환수 노력을 기울이지 않았다는 사실입니다. 안보를 걱정한다지만, 사실은 안보에 구멍을 그것도 커다랗게 내고 있던 사람들 장면 1,2,3은 그렇게 다른 듯 닮아 있습니다.')
print(nouns)

pos = kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^')
print(pos)
