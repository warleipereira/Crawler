import scrapy


class G1spiderSpider(scrapy.Spider):
    name = 'G1Spider'
    allowed_domains = ['g1.globo.com']
    start_urls = ['http://g1.globo.com/economia/tecnologia']

    def parse(self, response):
        page_title = response.css('Title::text').extract_first()
        yield {'Titulo':page_title}
       
