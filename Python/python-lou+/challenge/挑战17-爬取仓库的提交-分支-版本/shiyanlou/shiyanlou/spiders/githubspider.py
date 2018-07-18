# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class GithubspiderSpider(scrapy.Spider):
    name = 'githubspider'
      
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))


    def parse(self, response):
        for github in response.css('#user-repositories-list ul li'):
            item = ShiyanlouItem()
            item['name'] = github.xpath('.//div[1]/h3/a/text()').re_first(r'\n\s*([\w_-]*)')
            item['update_time'] = github.xpath('.//div[3]/relative-time/@datetime').extract_first()
            git_url = response.urljoin(github.xpath('.//div[1]/h3/a/@href').extract_first())
            request = scrapy.Request(git_url, callback=self.parse_otherinfo)
            request.meta['item'] = item
            yield request

    def parse_otherinfo(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('//ul[@class="numbers-summary"]/li[1]').xpath('.//span/text()').re_first('[^\d]*(\d+)[^\d]*')
        item['branches'] = response.xpath('//ul[@class="numbers-summary"]/li[2]').xpath('.//span/text()').re_first('[^\d]*(\d+)[^\d]*')
        item['releases'] = response.xpath('//ul[@class="numbers-summary"]/li[3]').xpath('.//span/text()').re_first('[^\d]*(\d+)[^\d]*')        

        yield item


 
