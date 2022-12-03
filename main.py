import requests

def send_wechat_all(msg):
    token = '3f0cbb16774649d7a6fd8186f28c1a3e' #前边复制到那个token
    title = '每月一号提醒交停车费'
    content = msg
    topic = '1001'
    url = 'http://www.pushplus.plus/send?token=' + token + '&title=' + title + '&content=' + content + '&topic=' + topic
    print(url)
    r = requests.get(url)
    print(r.text)

if __name__ == '__main__':
    msg = '今天是这个月1号，张小姐交停车费。\n' \
          '今天是这个月1号，张小姐交停车费。\n' \
          '今天是这个月1号，张小姐交停车费。\n'
    send_wechat_all(msg)
