import requests
import sys

def send_wechat_all(token, msg):
    title = '每月一号提醒交停车费'
    content = msg
    topic = '1001'
    url = 'http://www.pushplus.plus/send?token=' + token + '&title=' + title + '&content=' + content + '&topic=' + topic
    r = requests.get(url)
    print(r.text)

if __name__ == '__main__':
    token = sys.argv[1]
    msg = '今天是28号或1号，张小姐交停车费。\n' \
          '今天是这个月28号或1号，张小姐交停车费。\n' \
          '今天是这个月28号或1号，韩先生检查Glados签到。\n'
    send_wechat_all(token, msg)
