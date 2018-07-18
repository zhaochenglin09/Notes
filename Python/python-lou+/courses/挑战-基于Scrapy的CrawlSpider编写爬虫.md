## 挑战：基于 Scrapy 的 CrawlSpider 编写爬虫

在上一周的 Scarpy 课程中，我们编写的爬虫都是基于 scrapy.spiders 的，其实 scrapy.spiders 模块下还提供了不少其他类型的爬虫，CrawlSpider 就是比较常用的一种。相较于 Spider，CrawlSpider 最大的不同是多了一个 rules 属性。rules 是一个包含 Rule 对象的列表，每个 Rule 对象定义了如何从返回的页面解析接下来要爬取的页面链接的规则。Rule 对象的默认参数如下：

```
scrapy.spiders.Rule(link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=None)
```
