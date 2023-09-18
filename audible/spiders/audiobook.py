import scrapy
from audible.items import AudibleItem


class AudiobookSpider(scrapy.Spider):
    name = "audiobook"
    allowed_domains = ["audible.co.uk"]
    start_urls = ["https://www.audible.co.uk/search?node=19378442031&pageSize=50&sort=title-asc-rank&ref_pageloadid=DZdiSDMe1frKtFew&ref=a_search_c4_pageSize_3&pf_rd_p=2d6eb233-7e38-41ad-a242-da851f8f1999&pf_rd_r=V3DSWYZKJA5TRQBEGSMZ&pageLoadId=Q77HySqJuJi6wTgz&creativeId=ef56eba4-2dfe-4ca8-9612-8dd421243848"]

    def parse(self, response):
        books = response.css('li.bc-list-item.productListItem')
        for book in books:
            if book.css('li.bc-list-item h3 a.bc-link::text').get():
                yield from self.parse_item(book)

        next_page = response.css('li.bc-list-item span.nextButton a ::attr(href)').get()
        next_disabled = response.css('li.bc-list-item span.nextButton').get()
        if next_page is not None and 'bc-button-disabled' not in next_disabled:
            next_page_url = 'https://www.audible.co.uk' + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_item(self, response):
        book_item = AudibleItem()
        book_item['title'] = response.css('li.bc-list-item h3 a.bc-link::text').get()
        author_labels = response.css('li.bc-list-item.authorLabel')
        authors = []
        for label in author_labels:
            author_names = label.css('span.bc-text a.bc-link::text').getall()
            authors.extend(author_names)
        book_item['author'] = authors
        narrator_labels = response.css('li.bc-list-item.narratorLabel')
        narrators = []
        for label in narrator_labels:
            narrator_names = label.css('span.bc-text a.bc-link::text').getall()
            narrators.extend(narrator_names)
        book_item['narrator'] = narrators
        book_item['series'] = response.css('li.bc-list-item.seriesLabel span.bc-text a.bc-link::text').get()
        book_item['length'] = response.css('li.runtimeLabel span::text').get()
        book_item['release_date'] = response.css('li.releaseDateLabel span::text').get()
        book_item['language'] = response.css('li.languageLabel span::text').get()
        price_labels = response.css('div.adblBuyBoxPrice p.buybox-regular-price')
        prices = []
        for price in price_labels:
            actual_prices = price.css('span.bc-text.bc-size-base::text').getall()
            prices.extend(actual_prices)
        if len(prices) == 2:
            book_item['price'] = prices[1]
        else:
            book_item['price'] = None
        yield book_item
