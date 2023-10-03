from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date


import services.services as _services, schemas.sales as _schemas, schemas.product as _product


app = FastAPI()
_services.create_database()

@app.post("/sales/", response_model=_schemas.Sales)
def create_sale(sale: _schemas.SalesCreate, db : Session = Depends(_services.get_db)):
    return _services.createSale(db=db, sale=sale);

@app.get("/sales")
async def retrieve_sales_by_date_range(start_date: date, end_date: date, db: Session = Depends(_services.get_db)):
    try:
        sales = _services.get_sales_data_by_date_range(db, start_date, end_date)
        if not sales:
            raise HTTPException(status_code=404, detail="No sales data found within the specified date range")
        return sales
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/sales/product/{product_id}")
async def filter_sales_by_category(
    product_id: int, db: Session = Depends(_services.get_db)
):
    try:
        sales = _services.filter_sales_data_by_product(db, product_id)
        if not sales:
            raise HTTPException(
                status_code=404, detail="No sales data found for the specified category"
            )
        return sales
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/sales/analyze-revenue")
async def analyze_revenue(db: Session = Depends(_services.get_db)):
    revenue_analysis = _services.calculate_revenue_by_time_period(db)
    return revenue_analysis

@app.get("/sales/category")
async def access_sales_data_by_category(db: Session = Depends(_services.get_db)):
    sales_by_category = _services.get_sales_data_by_category(db)
    return sales_by_category

@app.get("/inventory")
def view_current_inventory_status(db: Session = Depends(_services.get_db)):
    try:
        inventory_status = _services.get_current_inventory_details(db)
        if not inventory_status:
            raise HTTPException(status_code=404, detail="No inventory data found")
        return inventory_status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/sales/compare")
async def compare_sales_revenue(db: Session = Depends(_services.get_db)):
    revenue_data = _services.compare_revenue(db)
    return revenue_data

@app.get("/inventory/low-stock")
async def get_low_stock_products_endpoint(db: Session = Depends(_services.get_db)):
    low_stock_products = _services.get_low_stock_products(db)
    return low_stock_products

@app.put("/inventory/update/{product_id}")
async def update_inventory_endpoint(product_id: int, quantity_change: int, db: Session = Depends(_services.get_db)):
    updated_product = _services.update_inventory_quantity(db, product_id, quantity_change)
    if updated_product:
        return updated_product
    else:
        raise HTTPException(status_code=404, detail="Product not found")
    
@app.get("/inventory/history/{record_id}")
async def get_inventory_record_endpoint(record_id: int, db: Session = Depends(_services.get_db)):
    inventory_record = _services.get_inventory_record_by_id(db, record_id)    
    if inventory_record:
        return inventory_record
    else:
        raise HTTPException(status_code=404, detail="Inventory record not found")
    
@app.get("/inventory/check-availability/{product_id}", response_model=bool)
async def check_product_availability(product_id: int , db: Session = Depends(_services.get_db)):
    return _services.check_availability_in_database(db, product_id)
     
@app.post("/product/register", response_model=_product.Product)
def registerPrduct(product: _product.ProductCreate, db : Session = Depends(_services.get_db)):
    return _services.registerProduct(db=db, product=product);

