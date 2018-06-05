from aip import AipNlp

APP_ID='10287527'
API_KEY='TZ5cSpQLK8QDPCa0HFyBcrWr'
SECRET_KEY='8lrfRVK4UdT4giuXqfy7gzmQOsweDeq2'

aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

#result = aipNlp.lexer('吃葡萄不吐2017年12月2日葡萄皮')
#result = aipNlp.wordEmbedding('漂亮')
#result = aipNlp.wordSimEmbedding('丑陋', '美丽')
result = aipNlp.sentimentClassify('百度肯定是一家丑陋的公司')
#result = aipNlp.commentTag('这面包味道还将就')

print(result)