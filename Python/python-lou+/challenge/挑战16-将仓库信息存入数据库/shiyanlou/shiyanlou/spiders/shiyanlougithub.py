# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import GithubItem


class ShiyanlougithubSpider(scrapy.Spider):
    name = 'shiyanlougithub'
    allowed_domains = ['github.com']
    
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))
        

    def parse(self, response):
        for github in response.css('#user-repositories-list ul li'):
            yield {
              'name': github.xpath('.//div[1]/h3/a/text()').re_first(r'\n\s*([\w_-]*)'),
              'update_time': github.xpath('.//div[3]/relative-time/@datetime').extract_first()
                  }
