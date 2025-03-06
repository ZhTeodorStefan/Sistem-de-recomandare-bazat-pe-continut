import scrapy

class GameSpider(scrapy.Spider):
    name = "games"
    start_urls = ['https://sandbox.oxylabs.io/products']

    def parse(self, response):
        for game in response.css('div.product-card'):
            yield {
                'title': game.css('a h4::text').get(),
                'price': game.css('div.price-wrapper::text').get(),
            }
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)