# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['http://www.baidu.com']
    start_urls = ['http://http://www.baidu.com/']

    def parse(self, response):
        pass
