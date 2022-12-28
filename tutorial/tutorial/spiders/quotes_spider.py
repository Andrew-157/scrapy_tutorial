import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/'
    ]

    def parse(self, response):
        """
        a method that will be called to handle the response downloaded for each of the requests made. 
        The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it.
        The parse() method usually parses the response, extracting the scraped data as dicts and also finding new URLs to follow
        and creating new requests (Request) from them.
        """
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as file:
            file.write(response.body)
        self.log(f'Saved file {filename}')
