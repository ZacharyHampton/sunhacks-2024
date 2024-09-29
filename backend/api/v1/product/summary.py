from .models import ProductType, ProductSummary
from ...core.mongo import db

def get_product_summary(uuid: str) -> ProductSummary:
    document = db.products.find_one({"uuid": uuid})