#coding=utf-8
import urllib2;
import sys;

from bs4 import BeautifulSoup;

# response = urllib2.urlopen("http://www.nitianxieshen.com/");
#
# print response.read();

# response = urllib2.urlopen("http://www.nitianxieshen.com/4.html");
# print response.read();

# soup = BeautifulSoup(response.read(),"html.parser");
# print soup.prettify();
#"内容"
#print soup.div.contents;
#单个属性
# print soup.div.children;

# for child in soup.div.children:
#     print child;
#所有子节点的内容
# for child in soup.descendants:
#     print child.string;
# print soup.find_all('div',class_='post_title')[0].text;
# print soup.find_all('div',class_='post_entry')[0].text;


file = r'.\test.txt';
i =1;
for i in range(1,1253):
    if(i>3 and i<6):
        print "cuowu";
    else:
        response = urllib2.urlopen("http://www.nitianxieshen.com/"+i.__str__()+'.html');
        soup = BeautifulSoup(response.read(), "html.parser");
        str1 = soup.find_all('div',class_='post_title')[0].text;
        str1 = str1 + soup.find_all('div',class_='post_entry')[0].text;
        print str1;