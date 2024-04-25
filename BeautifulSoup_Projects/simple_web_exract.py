import sys
print(sys.executable)

import requests
from bs4 import BeautifulSoup
import re
url = "https://www.newegg.com/yeston-RX7900XT-20GD6-sugar-YA/p/27N-0042-000G7?cm_sp=SH-_-946256-_-8-_-1-_-9SIAZUEJJW4639-_-gpu-_-gpu-_-1&Item=9SIAZUEJJW4639"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

result = doc.find('h1')
# result = doc.find_all(['h1','h2','h3'])
# final = result[1].parent
print(result)
