import requests
import os
import time
import re

header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
host = 'http://www.yoyone.net/'

source_fb = open('./tw_min_web.txt', 'r', encoding='utf-8')

result = []

"""
<a target="_blank" href="http://www.tsmc.com.tw" rel="nofollow"><b>台湾积体电路制造股份有限公司</b></a>
"""
for si in source_fb.readlines():
    tmp_web = si.strip()
    res = requests.get(host+tmp_web, headers=header)
    # print(res.text)
    tmp_result = re.findall(r'href=(.*?) rel=\"nofollow', res.text)
    print(tmp_result)
    result.append(tmp_result[0])

save_fb = open('./tw_web_result.txt', 'w', encoding='utf-8')
for ri in result:
    save_fb.write(ri)
    save_fb.write('\n')

save_fb.close()
