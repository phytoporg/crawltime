import scrapy

class BrietbartLinksSpider(scrapy.Spider):
    name = "bbhomelinks"

    def start_requests(self):
        urls = [ 'http://www.breitbart.com' ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        extracted = response.css('a::attr(href)').extract()
        for href in extracted:
            utf_href = href.encode('utf-8', 'replace')
            self.log(utf_href)
            filename = 'bb_hrefs.out'

            if href is extracted[0]:
                with open(filename, 'wb') as f:
                    f.write(utf_href + "\n")
            else:
                with open(filename, 'ab') as f:
                    f.write(utf_href + "\n")

