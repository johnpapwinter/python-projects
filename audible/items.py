import scrapy


class AudibleItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    narrator = scrapy.Field()
    series = scrapy.Field()
    length = scrapy.Field()
    release_date = scrapy.Field()
    language = scrapy.Field()
    price = scrapy.Field()
