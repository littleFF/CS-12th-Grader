import requests
import sys
import re
import os
import wordcloud
import imageio
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
from lxml import etree


headers = {
   'Referer': 'http://music.163.com',
   'Host': 'music.163.com',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'User-Agent': 'Chrome/10'
  }


def get_song_lyric(headers, lyric_url):
   res = requests.request('GET', lyric_url, headers=headers)
   if 'lrc' in res.json():
       lyric = res.json()['lrc']['lyric']
       new_lyric = re.sub(r'[\d:.[\]]', '', lyric)
       return new_lyric
   else:
       return ''
       print(res.json())

def remove_stop_words(f):
   stop_words = {"作词", "作曲", "编曲","" }
   for stop_words in stop_words:
       f = f.replace(stop_words, '')
   return f

def create_word_cloud(f):
   print('根据词频，开始生成词云!')
   mk = imageio.imread('qingzuo.jpg')
   f = remove_stop_words(f)
   cut_text = " ".join(jieba.cut(f, cut_all=False, HMM=True))
   wc = WordCloud(width=1000,
                  height=700,
                  background_color='white',
                  mask=mk,
                  font_path='msyh.ttc', )
   print(cut_text)
   wc.generate(cut_text)
   # 写词云图片
   image_color = wordcloud.ImageColorGenerator(mk)

   wc_color = wc.recolor(color_func=image_color)
   wc_color.to_file('陈奕迅词云.png')

def get_songs(artist_id):
   page_url = 'https://music.163.com/artist?id=' + artist_id
   res = requests.request('GET', page_url, headers=headers)
   html = etree.HTML(res.text)
   href_xpath = "//*[@id='hotsong-list']//a/@href"
   name_xpath = "//*[@id='hotsong-list']//a/text()"
   hrefs = html.xpath(href_xpath)
   names = html.xpath(name_xpath)
   song_ids = []
   song_names = []
   for href, name in zip(hrefs, names):
       song_ids.append(href[9:])
       song_names.append(name)
       print(href, ' ', name)
   return song_ids, song_names
# 设置歌手ID，陈奕迅为2116
artist_id = '2116'
[song_ids, song_names] = get_songs(artist_id)
# 所有歌词
all_word = ''
# 获取每首歌歌词
for (song_id, song_name) in zip(song_ids, song_names):
   # 歌词API URL
   lyric_url = 'http://music.163.com/api/song/lyric?os=pc&id=' + song_id + '&lv=-1&kv=-1&tv=-1'
   lyric = get_song_lyric(headers, lyric_url)
   all_word = all_word + ' ' + lyric
   print(song_name)
# 根据词频 生成词云
create_word_cloud(all_word)