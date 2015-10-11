from date import datetime
import re

import scrapy


class BaseSpider(scrapy.Spider):
    """
    Extend scrapy.Spider and add a few utility methods.
    """

    # Simple RegEx compiled to remove html tags.
    HTML_TAG_RE = re.compile(r'<[^>]*?>', flags=re.UNICODE)
    NON_NUMBER_RE = re.compile(r'[^\d.]', flags=re.UNICODE)
    MULTIPLE_WHITESPACE_RE = re.compile(r'\s+', flags=re.UNICODE)
    SPACE_AROUND_PUNC_MARK_RE = re.compile('\s+([,.;:])\s+', flags=re.UNICODE)
    LAT_LONG_RE = re.compile('LatLng\([^,],[^)])')

    TODAY = datetime.today()

    def get_type(self, text):
        text = self.HTML_TAG_RE.sub(' ', text)
        text = text.lower()
        if 'flat' in text:
            return 'flat'

    def get_rent(self, text):
        text = self.HTML_TAG_RE.sub(' ', text)
        return self.NON_NUMBER_RE.sub(' ', text)

    def get_desc(self, text):
        text = self.MULTIPLE_WHITESPACE_RE.sub(' ', text).strip()
        text = self.SPACE_AROUND_PUNC_MARK_RE.sub('\g<1> ', text)
        return text

    def get_available(self, text):
        text = self.HTML_TAG_RE.sub(' ', text)
        text = self.MULTIPLE_WHITESPACE_RE.sub(' ', text).strip()
        available = datetime.strptime(text, '%d %b')
        available.replace(year=self.TODAY.year)
        return available
