import scrapy
from ..items import BookscrapItem
class QuoteSpider(scrapy.Spider):
    name = 'books'
    page_number = 2
    start_urls = [
        'http://books.toscrape.com/catalogue/page-1.html'
    ]
    
    def parse(self, response):
        items = BookscrapItem()
        all_books = response.css(".product_pod")
        for i in all_books:
            book = i.css("a::attr(title)").extract()
            price = i.css(".price_color::text").extract()
            items['book_name'] = book
            items['price'] = price
            yield items
            
        next_page = 'http://books.toscrape.com/catalogue/page-'+str(QuoteSpider.page_number)+'.html'
        if next_page is not None:
            QuoteSpider.page_number +=1
            yield response.follow(next_page, self.parse)
        