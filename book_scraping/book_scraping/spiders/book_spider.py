import scrapy


class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    # Global start url
    global url 
    url = start_urls[0]

    def parse(self, response):
        books = response.css('article.product_pod')
        
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()
            if relative_url is not None:
            # Handle uncertained paths
                if 'catalogue/' in relative_url:
                    book_url = url + '/' + relative_url
                else:
                    book_url = url + '/catalogue/' + relative_url
                    
                yield response.follow(book_url, callback=self.parse_book_page)
            
        # Get next page path
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            # Handle uncertained paths
            if 'catalogue/' in next_page:
                next_page_url = url + '/' + next_page
            else:
                next_page_url = url + '/catalogue/' + next_page
                
            yield response.follow(next_page_url, callback=self.parse)
            
    def parse_book_page(self, response):
        rows = response.css("table tr")
        
        yield {
            'url': response.url,
            'title': response.css('.product_main h1::text').get(),
            'product_type': rows[1].css("td ::text").get(),
            'price_excl_tax': rows[2].css("td ::text").get(),
            'price_incl_tax': rows[3].css("td ::text").get(),
            'tax': rows[4].css("td ::text").get(),
            'availability': rows[5].css("td ::text").get(),
            'reviews': rows[6].css("td ::text").get(),
            'stars': response.css("p.star-rating").attrib['class'],
            'category': response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
            'description': response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
            'price': response.css('p.price_color ::text').get(),
        }