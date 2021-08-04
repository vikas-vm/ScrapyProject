# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DelhicovidScrapItem(scrapy.Item):
    hospital_name = scrapy.Field()
    available_beds_without_oxygen = scrapy.Field()
    available_beds_with_oxygen = scrapy.Field()
    available_icu_beds_without_ventilator = scrapy.Field()
    available_icu_beds_with_ventilator = scrapy.Field()
    hospital_poc_name = scrapy.Field()
    hospital_poc_number = scrapy.Field()
    last_updated_on = scrapy.Field()
    area = scrapy.Field()
    district = scrapy.Field()
    total_beds_without_oxygen = scrapy.Field()
    total_beds_with_oxygen = scrapy.Field()
    total_icu_beds_without_ventilator = scrapy.Field()
    total_icu_beds_with_ventilator = scrapy.Field()
