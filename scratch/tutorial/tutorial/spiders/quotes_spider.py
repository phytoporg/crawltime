import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [ 'http://www.breitbart.com' ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'bbart.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {0}'.format(filename))

