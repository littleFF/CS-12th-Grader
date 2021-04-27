import jieba
import requests
from lxml import etree
from matplotlib import pyplot as plt
from wordcloud import WordCloud

cut_text_lists = []

# 打开停用词文件生成停用词表
with open("./停用词.txt", "r", encoding="utf-8") as f:
    text_list = f.readlines()
    # 列表推倒式去除换行符
    stop_text_list = [x.replace("\n", "") for x in text_list]

# 目标网页链接
url = "https://www.douban.com/note/719193482/"

# header请求头防止网站拦截
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
}

# 发送请求获取内容并解码
content = requests.get(url, headers=headers).content.decode()

# 创建xpath解析对象
xp = etree.HTML(content)

# 取出每一段内容
text_list = xp.xpath("//div[@class='note']//p/text()")

for text in text_list:
    # 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
    cut_text_list = list(jieba.cut(text))
    new_cut_text_list = []
    for t in cut_text_list:
        if t not in stop_text_list:
            new_cut_text_list.append(t)

    cut_text_lists.extend(new_cut_text_list)

# 将分词结果转换回字符串
cut_text = " ".join(cut_text_lists)

wordcloud = WordCloud(
    # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
    # font_path="C:/Windows/Fonts/simfang.ttf",
    font_path="/System/Library/Fonts/PingFang.ttc",
    # 设置了背景，宽高
    background_color="white", width=2000, height=1200).generate(cut_text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('词云图.png')

