from tfmkt.spiders.common import BaseSpider
from scrapy.shell import inspect_response # required for debugging

default_confederation_hrefs = [
  '/wettbewerbe/europa',
  '/wettbewerbe/europa?page=2',
  '/wettbewerbe/amerika'
]

class ConfederationsSpider(BaseSpider):
    name = 'confederations'

    def scrape_parents(self):
      return [ {'type': 'root', 'href': ""} ]

    def parse(self, response, **kwargs):
      for href in default_confederation_hrefs:
        yield {'type': 'confederation', 'href': href}
