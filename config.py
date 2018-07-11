import os
# configuration
CONFIG = {
    'pagename': [('jtbcnews'), ('chosun')],
    'common': {
        'since': '2017-01-01',
        'until': '2017-12-31',
        'fetch': True,
        'result_directory': '__results__/crawling',
        'access_token': 'EAACEdEose0cBAPuKKvGoe5d4UU6xw4Mgc3zyeujc5ZAsMCg0MgzYX30QMQV4NvjBP2yRAZALQ4xxZCDXcSjRI6tWken6wHrkawckUS1wcmZADCmxwVZBM3goaNlVHw6IsQ4Wn9elpebZBygjZBHfSqDXwkkeIhQtym2SNVEi7miUPsunHtfdG7ZAWjPBLuHP3ZA3DqcS7cIwPewZDZD'
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])
