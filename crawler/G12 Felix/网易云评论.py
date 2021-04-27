# Requests模块和Json模块

import requests  # ---网页请求
import json  # ---格式转换


def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname'] + ':\n\n')
            file.write(each['content'] + '\n')
            file.write("---------------\n")

def get_comments(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
        'referer': 'https://music.163.com/'
    }
    params = "Brz3HT85JisY8LDEnLmxi / xmif2K6blJa6S98 / yJLqJC57FXl3 / X2 / N4o7f + rI6X + XrTVC7x8LcajFJFdaJGEYAzGbBN6WQLsJSqWbi5PYjJ0DHpXPSqZk0o / +GOJigre4SPFZy1sAQvV + BNovPMpsaKevgNxMftnwzEictv6k2arH0y5XLZZ0y8P3FNYYgZ + s70qhLJHf8B5bfjf23uSiFaclQFGpM / Sn202q / iHgxXSq4f7y1NkFXlXXMfNn8io09KCa1yynKed9W1ptPI5q4Jj + 5\
    FQQgDYyXKHAvl1SisUm3Pj8rtl + VIGJFvyIVE"
    encSecKey = "d180e107a8c7d417d1a27bc23f2321b97d1744df31c17415843a41015fbec1ae3b681d45fc3d98974f05e1b552d5a5b54c750637f68d0b36e74596211e8db6d9d9969b52589a57c48c98a1c87dfaf3f93a228be636def04e36fd8ea2fe4c345b0951a9fe5fc8043937b753bbe5339a7d7180b0813b31af734668ab6f08eaa8c5"
    data = {
        "params ": params,
        "encSecKey": encSecKey
    }
    # 获取任意一首歌的精彩评论

    name_id = url.split('=')[1]
    target_url = "https://music.163.com/api/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)

    res = requests.post(target_url, headers=headers, data=data)  # 传入它的关键字参数
    return res


def main():
    url = input("请输入链接地址：")
    res = get_comments(url)  # 返回给相关获取的网页资源
    get_hot_comments(res)


if __name__ == "__main__":
    main()

