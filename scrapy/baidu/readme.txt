1. 创建项目 scrapy startproject 项目名字
scrapy startproject baidu

2. 创建爬虫文件 scrapy genspider 爬虫文件名字 要爬取的网页
scrapy genspider baidupage www.baidu.com
    网页名字不惜要添加协议名

3. 运行爬虫代码 scrapy crawl 爬虫名字
    scrapy crawl baidupage

解决 robots.txt
注释 settings.py 中的 20 ROBOTSTXT_OBEY = True