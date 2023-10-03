from sqlalchemy import func
import database as _db
from sqlalchemy.orm import Session
import schemas.product as _product, schemas.sales as _sales ,models.models as _models, schemas.inventory as _inventory
from typing import List
from datetime import date, timedelta


def create_database():
    return _db.Base.metadata.create_all(bind=_db.engine)

def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def createSale(db: Session, sale : _sales.SalesCreate):
    db_sale = _models.Sales(**sale.dict())
    db.add(db_sale)
    db.commit()
    return db_sale

def get_sales_data_by_date_range(db: Session, start_date: date, end_date: date) -> List[_models.Sales]:
    filtered_sales = db.query(_models.Sales).filter(_models.Sales.SaleDateTime.between(start_date, end_date)).all()
    return filtered_sales

def filter_sales_data_by_product(db: Session, product_id: int) -> List[_models.Sales]:
    filtered_sales = db.query(_models.Sales).filter(_models.Sales.ProductID == product_id).all()
    return filtered_sales

def calculate_revenue_by_time_period(db: Session) -> _sales.RevenueAnalysis:
    today = date.today()
    one_week_ago = today - timedelta(days=7)
    one_month_ago = today - timedelta(days=30)
    one_year_ago = today - timedelta(days=365)

    daily_revenue = calculate_revenue(db, today, today)
    weekly_revenue = calculate_revenue(db, one_week_ago, today)
    monthly_revenue = calculate_revenue(db, one_month_ago, today)
    annual_revenue = calculate_revenue(db, one_year_ago, today)

    return _sales.RevenueAnalysis(
        daily_revenue=daily_revenue,
        weekly_revenue=weekly_revenue,
        monthly_revenue=monthly_revenue,
        annual_revenue=annual_revenue
    )

def calculate_revenue(db: Session, start_date: date, end_date: date) -> float:
    sales_within_period = db.query(_models.Sales).filter(_models.Sales.SaleDateTime.between(start_date, end_date))
    print("sales within ",sales_within_period)
    total_revenue = sum(sale.TotalRevenue for sale in sales_within_period)
    return total_revenue


def get_sales_data_by_category(db: Session) -> _sales.SalesByCategoryResponse:
    sales_data = (
        db.query(_models.ProductCategory.CategoryName, func.sum(_models.Sales.TotalRevenue))
        .join(_models.Sales, _models.Sales.ProductID == _models.ProductCategory.CategoryID)
        .group_by(_models.ProductCategory.CategoryName)
        .all()
    )

    result = [
        _sales.SalesCategoryData(category_name=category, total_sales=total_sales)
        for category, total_sales in sales_data
    ]

    return _sales.SalesByCategoryResponse(sales_data=result)

def get_current_inventory_details(db: Session) -> List[_models.InventoryRecords]:
    inventory_status = db.query(_models.InventoryRecords).all()
    return inventory_status

def compare_revenue(db: Session) -> dict[str, List[float]]:
    today = date.today()
    current_month = today.month
    current_year = today.year

    # Initialize dictionaries to store revenue data
    monthly_revenues = {}
    yearly_revenues = {}

    # Calculate monthly and yearly revenues
    for month in range(1, current_month + 1):
        start_date = date(current_year, month, 1)
        end_date = date(current_year, month, 28)  # Assuming an average month length

        monthly_revenue = calculate_revenue(db, start_date, end_date)
        monthly_revenues[start_date.strftime("%B")] = monthly_revenue

    for year in range(current_year - 1, current_year + 1):
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)

        yearly_revenue = calculate_revenue(db, start_date, end_date)
        yearly_revenues[str(year)] = yearly_revenue

    return {"monthly_revenues": monthly_revenues, "yearly_revenues": yearly_revenues}

def calculate_revenue(db: Session, start_date: date, end_date: date) -> float:
    sales_within_period = db.query(_models.Sales).filter(_models.Sales.SaleDateTime.between(start_date, end_date)).all()
    total_revenue = sum(sale.TotalRevenue for sale in sales_within_period)
    return total_revenue


def get_low_stock_products(db: Session) -> List[_product.Product]:
    low_stock_products = db.query(_models.Products).filter(_models.Products.CurrentInventoryQuantity <= _models.Products.LowStockThreshold).all()
    return low_stock_products

def update_inventory_quantity(db: Session, product_id: int, quantity_change: int) -> _product.Product:
    product = db.query(_models.Products).filter(_models.Products.ProductID == product_id).first()
    
    if product:
        new_quantity = product.CurrentInventoryQuantity + quantity_change
        product.CurrentInventoryQuantity = new_quantity
        db.commit()
        db.refresh(product)
        return product
    else:
        return None
    
def get_inventory_record_by_id(db: Session, record_id: int) -> _inventory.Inventory:
    return db.query(_models.InventoryRecords).filter(_models.InventoryRecords.RecordID == record_id).first()


def check_availability_in_database(db: Session, product_id: int) -> bool:
    product =  db.query(_models.Products).filter(_models.Products.ProductID == product_id).first()
    if product:
        return product.CurrentInventoryQuantity > 0
    return False

def registerProduct(db: Session, product : _product.ProductCreate):
    db_product = _models.Products(**product.dict())
    db.add(db_product)
    db.commit()
    return db_product