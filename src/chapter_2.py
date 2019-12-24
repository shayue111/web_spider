# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 10:20
# @Author  : wangtao
# @Email   : wangt@zhiyitech.cn
# @File    : chapter_2.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'lxml')

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
