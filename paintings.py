# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
#from scrapy.loader import ItemLoader
#from ebuy.items import EbuyItem

class PaintingsSpider(scrapy.Spider):
    name = 'paintings'
    allowed_domains = ['etsy.com']
    start_urls = ['https://www.etsy.com/in-en/c/art-and-collectibles/painting?ref=catnav-66']

    def parse(self, response):
        urls=response.xpath('//*[@class="responsive-listing-grid wt-grid wt-grid--block justify-content-flex-start pl-xs-0"]//a//@href').extract()
        for url in urls:
            yield Request(url,callback=self.parse_info)
            #yield{'url':url}

        next=response.xpath('//*[@class="wt-btn wt-btn--small wt-action-group__item wt-btn--icon"]/@href').extract_first()
        yield Request(next)

    def parse_info(self,response):
        name=response.xpath('//*[@data-component="listing-page-title-component"]//text()').extract_first()
        ratings=response.xpath('//*[@class="wt-text-body-03"]//text()').extract()
        cust_name=response.xpath('//*[@class="wt-text-link wt-mr-xs-1"]//text()').extract()
        review=response.xpath('//*[@class="wt-break-word"]//text()').extract()

        yield{'name':name,
        'ratings':ratings,
        'cust_name':cust_name,
        'review':review}
