from MAIN.Object.Product import *

def test_product_dao():
    mongo_uri = 'mongodb+srv://teodorstefanzaharia:OdTvBHwBaENZZiC0@main.g8ezz.mongodb.net/'
    mongo_db = 'testare'
    mongo_collection = 'initialTests'

    dao = ProductDAO(mongo_uri, mongo_db, mongo_collection)

    # Test - CREATE
    product_1 = ProductDTO("Laptop", 1500)
    dao.add_product(product_1)
    print("Product added:", product_1.to_dict())

    # Test - READ (get_all_products)
    products = dao.get_all_products()
    print("All products:", [product.to_dict() for product in products])

    # Test - READ (get_product_by_title)
    fetched_product = dao.get_product_by_title(product_1)
    print("Fetched product by title:", fetched_product.to_dict() if fetched_product else "Not found")

    # Test - UPDATE
    product_1.price = 1400
    dao.update_product(product_1)
    print("Product updated:", product_1.to_dict())

    # Test - DELETE
    dao.delete_product(product_1)
    print("Product deleted:", product_1.to_dict())

    dao.close_connection()

if __name__ == "__main__":
    test_product_dao()
