import scrapy


class AudiobookSpider(scrapy.Spider):
    name = "audiobook"
    allowed_domains = ["audible.co.uk"]
    start_urls = ["https://www.audible.co.uk/search?node=19378442031&pageSize=50&sort=title-asc-rank&ref_pageloadid=DZdiSDMe1frKtFew&ref=a_search_c4_pageSize_3&pf_rd_p=2d6eb233-7e38-41ad-a242-da851f8f1999&pf_rd_r=V3DSWYZKJA5TRQBEGSMZ&pageLoadId=Q77HySqJuJi6wTgz&creativeId=ef56eba4-2dfe-4ca8-9612-8dd421243848"]

    def parse(self, response):
        pass
