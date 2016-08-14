import http.client
import json

def youdao_translate(q=''):
    conn = http.client.HTTPSConnection('fanyi.youdao.com', timeout=10)
    conn.request("GET",'/openapi.do' + '?' + 'keyfrom=tagweb&key=881218182&type=data&doctype=json&version=1.1&q='+q)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)['translation'][0]

print(youdao_translate('hello'))
