# coding=utf-8
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

# 1.读入txt文本数据
with open("test.txt", 'r', encoding='utf-8', errors='ignore') as f:
           text=f.read()
 
# 2.分词
cut_text = " ".join(jieba.cut(text))
 
 # 3.生成词云
wc = WordCloud(
     font_path=r'.\simhei.ttf',
     background_color = 'white',
     width = 1000,
     height = 880,
).generate(cut_text)
 
# 4.显示词云图片
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()