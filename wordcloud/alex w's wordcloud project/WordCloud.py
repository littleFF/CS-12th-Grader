import jieba
import wordcloud
import imageio

mk = imageio.imread('qingzuo.jpg')
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        mask=mk,
                        font_path='msyh.ttc', )
f = open('斗破苍穹.txt', encoding='utf-8')
txt = f.read()
f.close()
txt_list = jieba.lcut(txt)
string = "".join(txt_list)
w.generate(string)

image_color = wordcloud.ImageColorGenerator(mk)

wc_color = w.recolor(color_func=image_color)
wc_color.to_file('斗破苍穹qq企鹅.png')