from pydantic import BaseModel
import datetime as _dt
from typing import List


class _SalesBase(BaseModel):
    SaleDateTime: _dt.datetime
    CustomerID: int
    SalespersonID: int
    PaymentMethod: str
    SalesRegion : str
    ProductID : int
    QuantitySold : int
    TotalRevenue : float


class SalesCreate(_SalesBase):
    pass

class Sales(_SalesBase):
    SalesID : int

class SalesCategoryData(BaseModel):
    category_name: str
    total_sales: float

class SalesByCategoryResponse(BaseModel):
    sales_data: List[SalesCategoryData]

class RevenueAnalysis(BaseModel):
    daily_revenue: float
    weekly_revenue: float
    monthly_revenue: float
    annual_revenue: float
