from persistent import Persistent

class Book(Persistent):
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price
