
import scrapy


class CraigSpider(scrapy.Spider):
    name = 'craigspider'
    start_urls = [
        'https://lasvegas.craigslist.org/search/sss?query=motorhome&sort=rel&min_price=1000&max_price=3000',
        'https://losangeles.craigslist.org/search/sss?query=motorhome&sort=rel&min_price=1000&max_price=3000']

    def parse(self, response):
        for result in response.css('.result-row'):
            title = result.css('.result-title ::text').get()
            cleanTitle = ''.join(c for c in title if c not in '\'')
            yield {
                'title': cleanTitle,
                'url': result.css('.result-title ::attr(href)').get(),
                'price': result.css('.result-price ::text ').get(),
                # 'img': result.css(".result-image img::attr(src)").get(),
                'date': result.css('.result-date ::text').get(),
            }

        for next_page in response.css('a.button.next'):
            yield response.follow(next_page, self.parse)
