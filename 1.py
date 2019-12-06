import urllib.request
import json

ak = 'Zfrdc6W1kV26DSGPqgZ31lGk'
sk = '6pZDZemZ8FHVMCdQGAitSfjVmEWy4e36'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (ak, sk)

request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')

response = urllib.request.urlopen(request)
content = response.read()

json_all = json.loads(content)
access_token = json_all['access_token']

url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s' % access_token
data = urllib.parse.urlencode({'url': 'https://www.python.org/static/img/python-logo.png'}).encode()
req = urllib.request.Request(url, method='POST')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')

res = urllib.request.urlopen(req, data).read().decode('utf-8')
ocr = json.loads(res)
for item in ocr['words_result']:
    print(item['words'])
