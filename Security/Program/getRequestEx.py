import urllib.parse
import urllib.request
url = 'https://d2zoxm4i0garux.cloudfront.net'
with urllib.request.urlopen(url) as response:  # GET
    content = response.read()
print(content)
