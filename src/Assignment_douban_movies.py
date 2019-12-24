# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 17:26
# @Author  : wangtao
# @Email   : wangt@zhiyitech.cn
# @File    : Assignment_douban_movies.py

"""
这是我自己想的作业，爬取豆瓣电影Top250
"""

import requests
from bs4 import BeautifulSoup
import re
from utils import *
import random

# def get_douban_top250(url):
headers = {'user-agent': random.choice(USER_AGENT_LIST)}

html = requests.get(url='https://movie.douban.com/top250', headers=headers)
soup = BeautifulSoup(html.content, 'lxml', from_encoding="utf8")

for movie in soup.find_all('div', {
    'class': 'item', 'class': 'pic'}):
    print(movie)
    # print(movie.get('div'))
    print(type(movie))
    print(movie.get('pic'))
    # print(movie.attrs['class'])
    break

# print(soup.find('div', {'id': 'content'}).find('ol', {'class': 'grid_view'}).find_all('div', {
#     'class': 'item'}).find_all('div'))
