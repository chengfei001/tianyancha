# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianyanchaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field()
    referer = scrapy.Field()
    legal_representative = scrapy.Field()
    management_forms = scrapy.Field()
    industry = scrapy.Field()
    type_of_enterprise = scrapy.Field()
    registration_no = scrapy.Field()
    org_code = scrapy.Field()
    unified_credit_code = scrapy.Field()
    taxpayer_identity_number = scrapy.Field()
    operating_period = scrapy.Field()
    registration_authority = scrapy.Field()
    registered_address = scrapy.Field()
    scope_of_business = scrapy.Field()

