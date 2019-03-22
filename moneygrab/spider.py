import re

import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class ProductSpider(scrapy.spiders.Spider):

    def parse(self, response):
        page = response.url.split("/")[-1]

        if re.search(r"\d{6,8}", page):
            filename = '../products/%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)

        le = LxmlLinkExtractor(unique=True)  # empty for getting everything, check different options on documentation
        for link in le.extract_links(response):
            yield Request(link.url, callback=self.parse)


def get_spider_for_company(company_config):
    return type(
        f"{company_config['name']}Spider",
        (ProductSpider,),
        {
            "name": company_config["name"],
            "allowed_domains": company_config["allowed_domains"],
            "start_urls": company_config["start_urls"]
        }
    )


def run_spider(company_config, limit=100):
    spider_class = get_spider_for_company(company_config, limit=limit)

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(spider_class)
    process.start()
