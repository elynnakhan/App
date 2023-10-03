from pydantic import BaseModel
import datetime as _dt
from typing import List

class _ProductBase(BaseModel):
    ProductName : str
    ProductDescription : str
    ProductCategoryID : int
    ProductPrice : float
    ManufacturerID : int
    CurrentInventoryQuantity : int
    LowStockThreshold : int
    DateAddedToInventory : _dt.datetime
    ProductImage : str

class ProductCreate(_ProductBase):
    pass

class Product(_ProductBase):
    ProductID : int
 

class ProductCategory(BaseModel):
    CategoryID : int
    CategoryName : str
    CategoryDescription :str
