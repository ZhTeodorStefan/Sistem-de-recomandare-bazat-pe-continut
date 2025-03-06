from pymongo import MongoClient
from .DTO import ProductDTO

class ProductDAO:
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_db]
        self.collection = self.db[mongo_collection]

    def close_connection(self):
        self.client.close()

    # CREATE
    def add_product(self, product_dto):
        self.collection.insert_one(product_dto.to_dict())

    # READ
    def get_all_products(self):
        products = self.collection.find({}, {"_id": 0})
        return [ProductDTO.from_dict(product) for product in products]

    def get_product_by_title(self, product_dto: ProductDTO):
        product = self.collection.find_one({"title": product_dto.title}, {"_id": 0})
        return ProductDTO.from_dict(product) if product else None

    # UPDATE
    def update_product(self, product_dto: ProductDTO):
        self.collection.update_one(
            {"title": product_dto.title},
            {"$set": product_dto.to_dict()}
        )

    # DELETE
    def delete_product(self, product_dto: ProductDTO):
        self.collection.delete_one({"title": product_dto.title})