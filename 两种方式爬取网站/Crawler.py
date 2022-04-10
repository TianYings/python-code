import requests
from retrying import retry
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver

#用xpath爬取
def x_path(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
    }
    resp = requests.get(url, headers=header)
    html_doc = resp.content.decode("UTF-8")
    html = etree.HTML(html_doc)
    cartoon_name = html.xpath("//p[@class='u-tt']/text()")
    img_src = html.xpath("//a[@class='u-card']/img/@data-src")
    for i in range(len(cartoon_name)):
        print(cartoon_name[i] + "---" + img_src[i])
    return "http://www.4399dmw.com"+html.xpath("//a[@class='next']/@href")[0] #这是判断下一页按钮是不是真正有下一页

#用靓汤爬取
def bs_4(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
    }

    resp = requests.get(url=url, headers=header)

    html_doc = resp.content.decode("UTF-8")

    soup = BeautifulSoup(html_doc)

    div = soup.findAll('div', class_='u-ct')
    for p in div:
        print(p.find('p', class_='u-tt').get_text().strip())


def main():
    x_path_url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-12-0/"
    bs4_url = "http://www.4399dmw.com/dh/list/jump/"

    #寻找一个页面的所有动漫名称,并全部遍历出来

    x_path(x_path_url)#用xpath爬取
    bs_4(bs4_url)#用靓汤爬取

if __name__ == "__main__":
    main()
