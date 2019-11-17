
import json
import requests
from requests.exceptions import RequestException
import re
import time

def get_one_page(url):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
        resp = requests.get(url,headers =headers )
        print(resp)
        if resp.status_code ==200:
            return resp.text
        return None

#解析數據，可正则匹配了7个信息，通过正则表达式提取出想要的结果
#获取排名：<dd>.*?board-index.*?>(\d+)</i>
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    #提取内容（将一页的电影都提出出来）
    items = re.findall(pattern, html)
    #print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

#写入文件，通过json库的dumps实现的字典序列化
#指定ensure_ascii=False，保证输出的结果是正文形式而不是unicode编码
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')



def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    print(url)
    html=get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


#分页爬取。爬取100条电影的信息
#需要遍历一下，给这个链接传入一个offset参数
i#f _name_ == '_main_'相当于Python模拟的程序入口
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        #可能会存在反爬虫，不能爬取太快
        time.sleep(1)