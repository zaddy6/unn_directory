# -*- coding: utf-8 -*-
from scrapy import Spider, Request


class UnnLecturesSpider(Spider):
    name = 'unn_lectures'
    allowed_domains = ['www.unn.edu.ng']
    start_urls = ['https://www.unn.edu.ng/internals/staff/show/']



    def parse(self, response):
        links = response.xpath('//*[@class="table table-striped"]/tbody/tr/td/a/@href').extract()

        for lin in links:
           yield Request(lin, callback=self.parse_dir_contents)

        url = response.xpath('/html/body/div/div[1]/div[2]/div[2]/section/p[1]/a[11respo]/@href').extract_first()
        if url:
            yield Request(url, self.parse)



    def parse_dir_contents(self, response):
        lecturer_name = response.xpath('//*[@class="col-sm-12"]//h4/text()').extract_first()
        department = response.xpath('//*[@class="table-striped"]//td/text()').extract()[0]
        faculty = response.xpath('//*[@class="table-striped"]//td/text()').extract()[1]
        designation = response.xpath('//*[@class="table-striped"]//td/text()').extract()[2]
        email = response.xpath('//*[@class="table-striped"]//td/text()').extract()[3]
        phone = response.xpath('//*[@class="table-striped"]//td/text()').extract()[4]



        yield {
            'name': lecturer_name,
            'department': department,
            'faculty': faculty,
            'designation': designation,
            'email': email,
            'phone': phone

        }