import re

fb = open('./source_page.txt', 'r', encoding='utf-8')

data = fb.read()
# print(data)
#<a href="https://www.finmart.com.tw/">全民電廠

result = re.findall(r'href="(http.*?)">', data.replace('\n', '：'))
print(result)

save_fb = open('tw_result.txt', 'w', encoding='utf-8')

for ri in result:
    save_fb.write(ri.replace('https://', '').replace('http://', '').split('/')[0])
    save_fb.write('\n')

save_fb.close()