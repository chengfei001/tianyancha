# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
import re
from scrapy import Selector
from ..items import TianyanchaItem

class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['m.tianyancha.com']
    start_urls = ['https://m.tianyancha.com']
    base_url = 'https://m.tianyancha.com'
    company_name = ''


    def parse(self, response):
        f = open('company_list', 'r')
        for obj in f:
            url = "https://m.tianyancha.com/search?key=%s" % obj
            yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        html = response.text
        urls_list = re.findall(re.compile(r"\"/company/\d+"), html)
        # print(urls_list)
        full_urls_list = [self.base_url + url[1:] for url in urls_list]  # 完整列表
        # n = 1
        for url in full_urls_list:
            # print(url)
            yield scrapy.Request(url, callback=self.parse_url)
        pass
        # print(response_content)
        # print(str(response_content,'utf-8'))

    def parse_url(self, response):
        selector = Selector(response)
        item_lines = selector.xpath("//div[@class='content-container pb10']/div[@class='item-line']")
        org_info = TianyanchaItem()
        org_info["company_name"] = selector.xpath("//div[@class='f18 new-c3 float-left']/text()").extract_first()
        # print(org_info["company_name"])
        org_info["referer"] = response.url

        for item_line in item_lines:
            if item_line.xpath("span/text()").extract()[0] == "法定代表人：":
                print(item_line.xpath("//a[@class=' f18 ']/text()").extract_first())
                org_info["legal_representative"] = item_line.xpath("//a[@class=' f18 ']/text()").extract_first()
                # item_line.xpath("//a[@class=' f18 ']/text()").extract_first()
            elif item_line.xpath("span/text()").extract_first() == "经营状态：":
                org_info["management_forms"] = item_line.xpath("span/text()").extract()[1]
            # elif item.xpath("span/text()").extract_first() == "注册时间：":
            #     org_info["registration_date"] = item.xpath("span/text()").extract()[1]
            # elif item.xpath("span/text()").extract_first() == "注册资本：":
            #     org_info["registered_capital"] = item.xpath("span/text()").extract()[1]
            elif item_line.xpath("span/text()").extract_first() == "行业：":
                org_info["industry"] = item_line.xpath("span/text()").extract()[1]
            elif item_line.xpath("span/text()").extract_first() == "企业类型：":
                org_info["type_of_enterprise"] = item_line.xpath("span/text()").extract()[1]
            elif item_line.xpath("span/text()").extract_first() == "工商注册号：":
                org_info["registration_no"] = item_line.xpath("span/text()").extract()[1]
            elif item_line.xpath("span/text()").extract_first() == "组织结构代码：":
                org_info["org_code"] = item_line.xpath("span/text()").extract()[1]
            elif item_line.xpath("span/text()").extract_first() == "统一信用代码：":
                org_info["unified_credit_code"] = item_line.xpath("span/text()").extract()[1]
            elif item_line.xpath("span/text()").extract_first() == "纳税人识别号：":
                org_info["taxpayer_identity_number"] = item_line.xpath("span/text()").extract()[1]
            elif item_line.xpath("span/text()").extract_first() == "经营期限：":
                org_info["operating_period"] = item_line.xpath("span/text()").extract()[1]
            # elif item.xpath("span/text()").extract_first() == "核准日期：":
            #     org_info["issue_date"] = item.xpath("span/text()").extract()[1]
            elif item_line.xpath("span/text()").extract_first() == "登记机关：":
                org_info["registration_authority"] = item_line.xpath("span/text()").extract()[1]
            elif item_line.xpath("span/text()").extract_first() == "注册地址：":
                org_info["registered_address"] = item_line.xpath("span/text()").extract()[1]
            # elif item_line.xpath("span/text()").extract_first() == "经营范围：":
            #     org_info["scope_of_business"] = item_line.xpath("span/text()").extract()[1]
            # if item.xpath("span/text()").extract()[0] == "注册地址：":
            #     print(item.xpath("span/text()").extract()[1])
        #     print()
        #     # if(item.xpath("//div[@class='item-line'/span/@class='left-text'"))
        yield org_info