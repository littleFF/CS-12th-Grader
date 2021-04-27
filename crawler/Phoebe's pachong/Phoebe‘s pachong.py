from bs4 import BeautifulSoup
from requests import Session
from re import sub,DOTALL
sess = Session()
txt=[]
url = '17754382.html'
res_file = open("demo.txt","a")
shu = []
def shuquge(url):
    res = sess.get('http://www.shuquge.com/txt/83203/'+url)
    soup = BeautifulSoup(res.content,'html.parser')
    h1 = soup.find('h1')
    div = soup.find('div', id="content")
    page = str(div)
    page = page.replace('<div class="showtxt" id="content">','')
    page = page.replace('<br/>','')
    page = sub('http.*','',page,0,DOTALL)
    shu.append(h1.text+'\n'+page)
    print(h1.text)
    res_file.write(h1.text)
    href = [i['href'] for i in soup.find_all('a') if i.text == '下一章'][0]
    if 'index' not in href:
        shuquge(href)
shuquge(url)
import jieba
import wordcloud
f = open("demo.txt", "r")
 
t = f.read()
f.close()
ls = jieba.lcut(t)
 
txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc"    
    )
w.generate(txt)
w.to_file("grwordcloud.png")