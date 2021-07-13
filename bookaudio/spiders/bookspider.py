import os
from pathlib import Path
import scrapy
from scrapy_splash import SplashRequest
from ..items import ChapterItem

class BookspiderSpider(scrapy.Spider):
    # Example use: 
    # scrapy crawl bookspider bookid=651-dune

    name = 'bookspider'
    allowed_domains = ['bookaudio.online']

    def __init__(self, bookid, *args, **kwargs):
        super(BookspiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://bookaudio.online/{bookid}.html']

    def start_requests(self):
        for url in self.start_urls:
            self.logger.info(f"Starting to scrap: {url}")

            lua_script = """
            function main(splash)
                splash:set_user_agent(splash.args.ua)
                assert(splash:go(splash.args.url))

                -- requires Splash 2.3  
                while not splash:select('.overview') do
                    splash:wait(0.1)
                end
                return {html=splash:html()}
            end"""

            yield SplashRequest(
                url, 
                self.parse, 
                endpoint='execute',
                args={
                    'lua_source': lua_script,
                    'ua': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
                }
            )

    def parse(self, response):
        book_name = response.css("h1.head span::text").extract_first()

        for chapter in response.css("div.overview li.track"):
            chapter_info = ChapterItem(
                chapter_num = chapter.css("::text").extract_first(),
                file_urls = chapter.css("::attr(data-url)").extract_first(),
                title = book_name
            )
            self.logger.info(f"Downloading {chapter_info.chapter_num} of {chapter_info.title}")
            yield chapter_info
