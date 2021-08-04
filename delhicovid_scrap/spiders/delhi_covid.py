import scrapy
import json
from ..items import DelhicovidScrapItem


class DelhiCovidSpider(scrapy.Spider):
    name = 'delhi_covid'
    start_urls = ['https://covidamd.com/data/covidamd.com/bed_data.json?_=0b16f86_20210727081037']

    def parse(self, response):
        items = DelhicovidScrapItem()
        for text in json.loads(response.text):
            items['hospital_name'] = text['hospital_name']
            items['available_beds_without_oxygen'] = text['available_beds_without_oxygen']
            items['available_beds_with_oxygen'] = text['available_beds_with_oxygen']
            items['available_icu_beds_without_ventilator'] = text['available_icu_beds_without_ventilator']
            items['available_icu_beds_with_ventilator'] = text['available_icu_beds_with_ventilator']
            items['hospital_poc_name'] = text['hospital_poc_name']
            items['hospital_poc_number'] = text['hospital_poc_number']
            items['last_updated_on'] = text['last_updated_on']
            items['area'] = text['area']
            items['district'] = text['district']
            items['total_beds_without_oxygen'] = text['total_beds_without_oxygen']
            items['total_beds_with_oxygen'] = text['total_beds_with_oxygen']
            items['total_icu_beds_without_ventilator'] = text['total_icu_beds_without_ventilator']
            items['total_icu_beds_with_ventilator'] = text['total_icu_beds_with_ventilator']

            yield items

