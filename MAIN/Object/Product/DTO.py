class ProductDTO:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def to_dict(self):
        return {"title": self.title, "price":self.price}

    @classmethod
    def from_dict(cls, data):
        return cls(title=data.get("title"), price=data.get("price"))