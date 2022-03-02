# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    target_pass = 'cf0d678b9a0fb10c4a6ba5e949ac9ff7'


    #读取密码文件
    password_fb = open('./password_result.txt', 'r', encoding='utf-8')

    for si in password_fb.readlines():
        print(si)
        si = si.strip()
        _, user, pwd = si.split()
        count = 0

        fb = open('./lib/密码字典4952222条.txt', 'r', encoding='utf-8')
        for line in fb.readlines():
            count += 1
            tmp = hashlib.md5()
            tmp.update(line.strip().encode('utf-8'))
            if tmp.hexdigest().lower() == pwd:
                print('{} {} {}'.format(user, pwd, line))
                print('done')
                break

            if count % 1000000 == 0:
                print('当前执行到第{}行：{}: {}'.format(count, line.strip(), tmp.hexdigest().lower()))

