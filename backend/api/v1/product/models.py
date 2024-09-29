from pydantic import BaseModel, AnyUrl
from enum import Enum

class ProductType(str, Enum):
    book = "book"
    skis = "ski"
    phone = "phone"


class ProductTypeToCollection(str, Enum):


class ProductSummary(BaseModel):
    uuid: str
    title: str
    image_url: AnyUrl
