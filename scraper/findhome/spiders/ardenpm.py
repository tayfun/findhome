# -*- coding: utf-8 -*-
import scrapy

from findhome.items import Property
from findhome.spiders.base import BaseSpider


class ArdenpmSpider(BaseSpider):
    name = "ardenpm"
    allowed_domains = ["ardenpm.co.uk"]
    start_urls = (
        'http://www.ardenpm.co.uk/property/',
    )

    def parse(self, response):
        """
        Parses search results page.
        """
        property_links = response.css('div.prop-details a::attr("href")')
        for href in property_links:
            url = href.extract()
            # All links start with property in Arden
            if not url.startswith('property'):
                continue
            yield scrapy.Request(url, callback=self.parse_property_detail_page)
        next_page = response.xpath('//a[text()=">>"]/@href')
        if next_page:
            url = next_page[0].extract()
            if url.startswith('property'):
                yield scrapy.Request(url, callback=self.parse)

    def parse_property_detail_page(self, response):
        desc = ''.join(
            response.css("div.post div.feat-list p::text").extract())
        desc = self.get_desc(desc)
        type = ''.join(response.css("div.post h1::text").extract())
        type = self.find_type(type)
        rent = ''.join(response.css('#rent-col::text').extract())
        rent = self.find_rent(rent)
        bedrooms = ''.join(response.css('#roomsCol .rooms::text').extract())
        bedrooms = int(bedrooms)
        available = ''.join(response.css('#date-block .date').extract())
        available = self.get_date(available)
        council_tax = ''.join(response.css('#CtaxCol .rooms::text').extract())
