from products import dao
from typing import List


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: dict) -> 'Product':
        """Create a Product instance from a dictionary."""
        return cls(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> List[Product]:
    """Fetch all products from the database and return them as a list of Product objects."""
    products = dao.list_products()
    return [Product.load(product) for product in products]


def get_product(product_id: int) -> Product:
    """Fetch a single product by its ID."""
    product_data = dao.get_product(product_id)
    if product_data is None:
        raise ValueError(f"Product with ID {product_id} not found.")
    return Product.load(product_data)


def add_product(product: dict) -> None:
    """Add a new product to the database."""
    required_keys = ['id', 'name', 'description', 'cost', 'qty']
    if not all(key in product for key in required_keys):
        raise ValueError(f"Product dictionary must contain the following keys: {', '.join(required_keys)}")
    dao.add_product(product)


def update_qty(product_id: int, qty: int) -> None:
    """Update the quantity of a product."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
