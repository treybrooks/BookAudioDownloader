# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass

@dataclass
class ChapterItem:
    chapter_num: str
    file_urls: str
    title: str

