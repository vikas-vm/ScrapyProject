# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class DelhicovidScrapPipeline:
    def __init__(self):
        self.conn = sqlite3.connect("sqlite3.db")
        self.curr = self.conn.cursor()
        # self.create_table()

    def create_table(self):
        state = self.curr.execute("""DROP TABLE IF EXISTS hospitals""")
        self.curr.execute("""
            CREATE TABLE hospitals(
                hospital_name text,
                available_beds_without_oxygen text,
                available_beds_with_oxygen text,
                available_icu_beds_without_ventilator text,
                available_icu_beds_with_ventilator text,
                hospital_poc_name text,
                hospital_poc_number text,
                last_updated_on text,
                area text,
                district text,
                total_beds_without_oxygen text,
                total_beds_with_oxygen text,
                total_icu_beds_without_ventilator text,
                total_icu_beds_with_ventilator text
            )
        """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO hospitals VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            item['hospital_name'],
            item['available_beds_without_oxygen'],
            item['available_beds_with_oxygen'],
            item['available_icu_beds_without_ventilator'],
            item['available_icu_beds_with_ventilator'],
            item['hospital_poc_name'],
            item['hospital_poc_number'],
            item['last_updated_on'],
            item['area'],
            item['district'],
            item['total_beds_without_oxygen'],
            item['total_beds_with_oxygen'],
            item['total_icu_beds_without_ventilator'],
            item['total_icu_beds_with_ventilator']
        ))
        self.conn.commit()
