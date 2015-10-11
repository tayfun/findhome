# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Property(scrapy.Item):
    description = scrapy.Fields()
    # Defines if the property is a flat, detached house etc.
    type = scrapy.Field()
    rent = scrapy.Field()
    bedrooms = scrapy.Fields()
    available = scrapy.Fields()
    council_tax = scrapy.Fields()
    lat = scrapy.Fields()
    lng = scrapy.Fields()
    agent = scrapy.Fields()
    url = scrapy.Fields()
    landlord_reg_no = scrapy.Fields()
