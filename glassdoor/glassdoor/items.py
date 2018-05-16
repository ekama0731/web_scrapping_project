# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GlassdoorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field(
    job_title = scrapy.Field()
    company_name = scrapy.Field()
    job_location = scrapy.Field()
    rating = scrapy.Field()
    salary_estimate= scrapy.Field()
    salary_low = scrapy.Field()
    salary_high = scrapy.Field()
    company_info= scrapy.Field()


