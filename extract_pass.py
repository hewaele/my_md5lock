import re
import os

if __name__ == '__main__':
    source_data_path = r'E:\hw\fh_work\业务\广州工作\20211101梅州涉诈网址\20211102v3'
    result = []
    for r, p, files in os.walk(source_data_path):
        for file in files:
            if file.endswith('http'):
                tmp_fb = open(os.path.join(r, file), 'r', encoding='utf-8')
                text = tmp_fb.read().replace('\n', '：')
                # print(text)
                tmp_result = re.findall('Host:(.*?)：.*&user=(.*?)&pass=(.*?)&', text)
                if tmp_result and tmp_result[0] not in result:
                    result.append(tmp_result[0])
                tmp_fb.close()

    result_data_fb = open('./password_result.txt', 'w', encoding='utf-8')
    print(result)
    for ri in result:
        result_data_fb.write('\t'.join(list(ri)))
        result_data_fb.write('\n')
    result_data_fb.close()
