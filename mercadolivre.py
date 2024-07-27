import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = ["http://www.mercadolivre.com.br/"]

    def parse(self, response):
        pass
