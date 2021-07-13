# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pathlib import Path
from urllib.parse import urlparse
import scrapy
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
import logging

class BookaudioPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return f"{item.title}/{item.chapter_num}"

    def get_media_requests(self, item, info):
        file_url = item.file_urls if "://" in item.file_urls else "http://" + item.file_urls
        yield scrapy.Request(file_url)
