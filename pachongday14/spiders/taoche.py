# -*- coding: utf-8 -*-
import scrapy
from ..city import CITY_CODE,CAR_CODE_LIST
from ..items import Pachongday14Item

class TaocheSpider(scrapy.Spider):
    name = 'taoche'
    allowed_domains = ['taoche.com']
    start_urls = []

    for city in CITY_CODE:
        for car in CAR_CODE_LIST:
            url="https://{}.taoche.com/{}/".format(city,car)
            start_urls.append(url)
    print(len(start_urls))


    def parse(self, response):
        max_page = response.xpath('//div[@class="paging-box the-pages"]/div/a[last()-1]/text()').extract()
        if max_page:
            page = int(max_page[0])
        else:
            page = 1

        for i in range(1,page+1):
            url = response.url+'?page=%d#pagetag'%i
            yield scrapy.Request(url=url,callback=self.parse1)

    def parse1(self,response):
        #获取整个车的信息：
        car_info_list = response.xpath('//ul[@class="gongge_ul"]/li')
        for car in car_info_list:
            item = Pachongday14Item()
            #标题：
            title = car.xpath('.//div[@class="gongge_main"]/a/span/text()').extract()[0]
            item['title']=title
            #车程：
            mile = car.xpath('.//div[@class="gongge_main"]/p/i[2]/text()').extract()[0]
            item['mile']=mile
            #详情页：
            detail_url = 'https:'+car.xpath('.//div[@class="gongge_main"]/a/@href').extract()[0]
            item['detail_url']=detail_url

            yield scrapy.Request(url=detail_url,callback=self.parse2,meta={'data':item},dont_filter=False)

    def parse2(self,response):
        print("1111111111111",response.url)
        item = response.meta['data']
        pl = response.xpath('//div[@class="summary-attrs"]/dl[3]/dd/text()').extract()[0]
        item['pl']=pl
        time = response.xpath('//div[@class="summary-attrs"]/dl[1]/dd/text()').extract()[0]
        item['time']=time
        add = response.xpath('//div[@class="summary-attrs"]/dl[4]/dd/text()').extract()[0]
        item['add'] =add
        yield item