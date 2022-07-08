from email import contentmanager
import urllib.parse
import urllib.request
info = {'user': 'tim', 'passwd': '31337'}
url = ''
data = urllib.parse.urlencode(info).encode()  # 바이트 형식으로 변환돼 data에 저장

print(data)
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:  # POST
    content = response.read()
print(content)
