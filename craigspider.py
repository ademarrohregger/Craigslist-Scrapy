
import scrapy


class CraigSpider(scrapy.Spider):
    name = 'craigspider'
    start_urls = ['https://lasvegas.craigslist.org/search/sss?query=motorhome']

    def parse(self, response):
        for title in response.css('.result-title'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.button.next'):
            yield response.follow(next_page, self.parse)
