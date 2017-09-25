# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 8 / 2
from scrapy.cmdline import execute
import sys
import os

# 相关官方文档：https://doc.scrapy.org/en/1.3/topics/commands.html?highlight=genspider
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "zhihu"])
