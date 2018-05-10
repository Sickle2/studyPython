#coding=utf-8
import urllib2;
import sys;

from bs4 import BeautifulSoup;

class Xiaoshuodownload:
    def __init__(self):
        #在页面抓取文件
        self.homeUrl="http://www.nitianxieshen.com/";

    def _get_next_page(self,num):
        self.page=self.homeUrl+num.__str__()+".html";


    def get_text(self):
        #获取html页面
        self.response = urllib2.urlopen(self.page);
        #使用beautifulsoup解析页面
        self.soup = BeautifulSoup(self.response.read(),"html.parser");

if __name__ == '__main__':
    test = Xiaoshuodownload();
    file = r'.\test.txt';
    i=1;
    for i in range(1,1253):
        if (i > 3 and i < 6):
            print "cuowu";
        else:
            test._get_next_page(i);
            test.get_text();
            text1 = test.soup.find_all('div',class_='post_title')[0].text;
            text2 = test.soup.find_all('div', class_='post_entry')[0].text;
