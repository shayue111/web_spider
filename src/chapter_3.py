# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 11:59
# @Author  : wangtao
# @Email   : wangt@zhiyitech.cn
# @File    : chapter_3.py

from utils import *
import re

pages = set()


def getLinks(pageUrl):
    global pages
    bs = get_response('http://en.wikipedia.org{}'.format(pageUrl))
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                newPage = link.attrs['href']
                print('-' * 20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('')
