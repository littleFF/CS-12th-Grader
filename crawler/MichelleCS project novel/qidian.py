# -*- coding: utf-8 -*-
# @File:       |   qidian.py 
# @Date:       |   2021/1/4 
# @Author:     |   ThinkPad
# @Desc:       |  爬取起点小说网站  黎明之剑  url=https://book.qidian.com/info/1010400217#Catalog
import json
import requests
import pandas as pd
from lxml import etree


def get_content(url, name):
    '''
    根据小说的链接，获取小说内容
    @param url:小说章节所对应的链接
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'cookie': '_yep_uuid=4e441d02-bfc5-30d2-1b28-3b766a05f108; _csrfToken=19xAZYByGcQNmkh2TTEblRhaZ0CVksJF8NejLn0E; newstatisticUUID=1609741800_513654948; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; e1=%7B%22pid%22%3A%22qd_P_all%22%2C%22eid%22%3A%22qd_B58%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_xianxia%22%2C%22eid%22%3A%22qd_A169%22%2C%22l1%22%3A40%7D; rcr=1010400217%2C1024211253%2C1025437931; bc=1025437931%2C1024211253%2C1010400217; pageOps=1; lrbc=1010400217%7C403440812%7C0%2C1024211253%7C599547453%7C0%2C1025437931%7C626353936%7C0; floatOp=12'
    }
    res = requests.get(url, headers=headers)
    info = []
    if 200 == res.status_code:
        res = res.content.decode()
        html = etree.HTML(res)
        head = html.xpath('.//span[@class="content-wrap"]//text()')
        content = html.xpath('.//div[@class="read-content j_readContent "]//text()')
        content = [x.replace(' ', '').replace('点击书签后，可收藏每个章节的书签，“阅读进度”可以在个人中心书架里查看', '') for x in content]
        content = list(filter(None, content))
        info.extend(head)
        info.extend(content)
        print(info)
        with open("./黎明之剑/{}.txt".format(name), "w", encoding='utf-8') as f:
            f.writelines(info)


def get_chapter(chapter_url):
    '''
    获取小说章节对应的链接和章节名称
    @return:
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'cookie': '_csrfToken=19xAZYByGcQNmkh2TTEblRhaZ0CVksJF8NejLn0E; newstatisticUUID=1609741800_513654948; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; e1=%7B%22pid%22%3A%22qd_P_all%22%2C%22eid%22%3A%22qd_B58%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_xianxia%22%2C%22eid%22%3A%22qd_A169%22%2C%22l1%22%3A40%7D; rcr=1010400217%2C1024211253%2C1025437931; bc=1025437931%2C1024211253%2C1010400217; lrbc=1010400217%7C404259292%7C0%2C1024211253%7C599547453%7C0%2C1025437931%7C626353936%7C0'
    }
    res = requests.get(chapter_url, headers=headers)
    if 200 == res.status_code:
        res = res.content.decode()
        json_info = json.loads(res)
        print(json_info)
        # 获取章节
        storyInfo = json_info['data']['vs'][0]['cs']
        nameList = []
        urlList = []
        for info in storyInfo:
            nameList.append(info['cN'])
            urlList.append('https://read.qidian.com/chapter/' + info['cU'])
        df = pd.DataFrame({
            '章节': nameList,
            '链接': urlList
        })
        print(df)
        for index, info in df.iterrows():
            url = info['链接']
            name = info['章节']
            print(url, name)
            get_content(url, name)


if __name__ == '__main__':
    url = 'https://book.qidian.com/ajax/book/category?_csrfToken=19xAZYByGcQNmkh2TTEblRhaZ0CVksJF8NejLn0E&bookId=1010400217'
    get_chapter(url)
