# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from MAIN.Object.Product.DAO import ProductDAO
from MAIN.Object.Product.DTO import ProductDTO

class MongoDBPipeline:

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.dao = ProductDAO(mongo_uri, mongo_db, mongo_collection)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        # conexiune gestionata in DAO
        pass

    def close_spider(self, spider):
        self.dao.close_connection()

    def process_item(self, item, spider):
        product = ProductDTO(title=item["title"], price=(item["price"]))
        self.dao.add_product(product)
        return item