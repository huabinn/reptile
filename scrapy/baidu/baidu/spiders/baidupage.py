import scrapy


class BaidupageSpider(scrapy.Spider):
    # 爬虫名，用于运行的时候使用的值
    name = 'baidupage'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 在 allowed_domains 基础上 加上协议名字 http:// 及 末尾的 /
    start_urls = ['http://www.baidu.com/']

    # 执行了start_urls之后执行的方法 方法返回 response 对象
    # 相当于 response = urllib.request.urlopen(url)
    def parse(self, response):
        print("binn----------------------------")
        pass
