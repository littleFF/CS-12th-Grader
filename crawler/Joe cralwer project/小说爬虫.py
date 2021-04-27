import requests    #导入用于发送请求的库
import re    #导入筛选出小说内容的库
#小说地址，包含章节目录的信息
book_url = 'http://www.xbiquge.la/10/10489/'

#用于后面拼接小说章节地址
base_url='http://www.xbiquge.la'

'''
    第一章小说地址:http://www.xbiquge.la/10/10489/4535761.html
    第二章小说地址:http://www.xbiquge.la/10/10489/9683462.html
    第三章小说地址:http://www.xbiquge.la/10/10489/9687224.html
'''

#response_1 是通过 requests 库 get 方法向小说网址发出请求之后得到的响应，而 response_1.text 表示纯文本
response_1=requests.get(book_url)

#下面一步骤是设置编码格式，因为小说采用 utf-8 编码，一般遇到乱码可以用下面一句代码来解决
response_1.encoding='utf-8'
#小说章节目录相关信息所在的文本
chapter=response_1.text
#下面的一段注释是 response_1.text 的部分内容
'''
<dd><a href='/10/10489/4534454.html' >写在连载前</a></dd>
                <dd><a href='/10/10489/4535761.html' >第一章 我要减肥！</a></dd>
                <dd><a href='/10/10489/9683462.html' >第二章 王宝乐，你干了什么！</a></dd>
                <dd><a href='/10/10489/9687224.html' >第三章 好同学，一切有我！</a></dd>
'''

regx="<dd><a href='(.*)' >"
#该正则表达是获取形如 /10/10489/9683462.html 格式的文本，用于后期拼接成小说具体章节地址
chapter_href_list=re.findall(regx, response_1.text)

#定义一个列表来存储小说章节地址
chapter_url_list=[]
#遍历 chapter)href)list 中的所有元素并与 base_url 一起拼接成小说地址
for i in chapter_href_list:
    url=base_url+i
    chapter_url_list.append(url)

#以下是提取正文内容的正则表达式，是通过分析小说内容特点的源码来写的
content_regx='<br />&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'

'''小说部分内容如下，
<br />&nbsp;&nbsp;&nbsp;&nbsp;好在随着他的苏醒，名叫周小雅的小白兔对他照顾无微不至，杜敏也罕见的没有与他针锋相对，这就让
<br />&nbsp;&nbsp;&nbsp;&nbsp;他唯独郁闷的，就是在之后的几天里，团队众人穿梭丛林，寻找其他同学的路上，柳道斌也不知道吃错了什么药，也许是因为之前的事情愧疚，所以一路上遇到一些小危机，总是抢着带人出手，迅速化解，使得本就虚弱的王宝乐，没有丝毫
<br />&nbsp;&nbsp;&nbsp;&nbsp;偏偏又没有出现如蛇群那般大的事件，这就让王宝乐觉得自己一身通天的本领，却没有用武之地，满是
<br />&nbsp;&nbsp;&nbsp;&nbsp;“这柳道斌再这么下去，说不定隐藏的考核分，就比我高了！”到了最后，王宝乐都焦急了，不过这种
'''
#内容特点分析
'''
    我们很容易观察到文字都包含在 <br />&nbsp;&nbsp;&nbsp;&nbsp;和<br />之间，故可以用 (.*?)
    来代表文字内容，其中 . 代表任意字符(除了换行)， * 代表任意多个字符, ?代表非贪婪匹配， ()是为了将内容包含
    起来，使匹配结果仅包含括号里面的内容
'''


'''
    这是小说章节名称所在位置
    <h1>正文卷 第三章 好同学，一切有我！</h1>
'''
#所以匹配出小说章节标题的正则表达式如下
title_regx='<h1>(.*?)</h1>'

#设置小说保存路径
##如果爬取的时候出现permission deny，请修改下面的sava_path,例如可以直接修改为 save_path="三寸人间.txt"
#这样以后爬取的小说会与Python文件保存在同一个路径
save_path='三寸人间.txt'

#定义一个变量来计数已经爬取的小说的数目
count=0
##如果爬取的时候出现permission deny，请修改上面的sava_path,例如可以直接修改为 save_path="三寸人间.txt"
#这样以后爬取的小说会与Python文件保存在同一个路径
#with open 语句的作用是在 C 盘创建一个叫做三寸人间.txt 的文件，'a+'表示文件以追加的形式写入，
#encoding="utf-8"是为了防止写入错误
with open (save_path,'a+',encoding="utf-8") as f:
#从存放小说章节地址的列表中依次去除小说地址，让requests通过get方法去取货
    for x in chapter_url_list:
        #向小说章节所在地址发送请求并获得响应
        response_2=requests.get(x)

        #设定编码，解决乱码
        response_2.encoding='utf-8'

        #小说标题,匹配到的是列表
        title=re.findall(title_regx, response_2.text)

        #正文内容，匹配到的是列表
        content=re.findall(content_regx, response_2.text)

        #写入小说标题
        f.write('--------'+title[0]+'--------'+'\n')

        #将小说内容这个列表中的所有元素写入文件，每写入一个就换一次行
        for e in content:
            f.write(e+'\n')
        #每成功写入一章 count 就加 1
        count+=1
        # format函数用于格式化输出
        print('第{}章爬取完毕！'.format(count))