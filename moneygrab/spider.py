import scrapy


def get_spider_for_company(domain):
    return scrapy.spiders.Spider(
        name=domain,
        allowed_domains=[domain],
        start_urls=[domain]
    )


spider = get_spider_for_company("uk.burberry.com")
spider.start_requests()
