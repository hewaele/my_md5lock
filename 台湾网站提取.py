import requests
import re
from bs4 import BeautifulSoup
import time

result = []
header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
host = 'http://www.yoyone.net/'

for i in range(1, 24):
    res = requests.get('http://www.yoyone.net/world_state.asp?id=151&sid=&PageNo={}'.format(i), headers=header)
    content = res.content
    # print(content)
    tmp_result = re.findall('world_site\.asp\?SiteID=[\d]{4}', str(content))
    result.extend(tmp_result)
    print(tmp_result)
    time.sleep(2)

fb = open('tw_min_web.txt', 'w', encoding='utf-8')
for ri in result:
    fb.write(ri)
    fb.write('\n')
fb.close()