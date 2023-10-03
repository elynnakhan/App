from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import database as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(db.Base):
    __tablename__ = "Products"

    ProductID = Column(Integer, primary_key=True, index=True)
    ProductName = Column(String(255))
    ProductDescription = Column(String(255))
    ProductCategoryID = Column(Integer, ForeignKey('ProductCategory.CategoryID'))  # Establish the ProductCategory relationship
    ProductPrice = Column(Float)
    ManufacturerID = Column(Integer, ForeignKey('Manufacturers.ManufacturerID'))  # Establish the Manufacturer relationship
    CurrentInventoryQuantity = Column(Integer)
    LowStockThreshold = Column(Integer)
    DateAddedToInventory = Column(DateTime)
    ProductImage = Column(String(255))

    category = relationship("ProductCategory", back_populates="products")
    manufacturer = relationship("Manufacturer", back_populates="products")
    inventory_records = relationship("InventoryRecords", back_populates="product")
    sales_transaction_details = relationship("Sales", back_populates="product")

class Sales(db.Base):
    __tablename__ = "Sales"

    SalesID = Column(Integer, primary_key=True, index=True)
    SaleDateTime = Column(DateTime)
    CustomerID = Column(Integer, ForeignKey('Customers.CustomerID'))  # Establish the Customer relationship
    SalespersonID = Column(Integer, ForeignKey('Users.UserID'))  # Establish the Salesperson relationship
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))  # Establish the Product relationship
    QuantitySold = Column(Integer)
    TotalRevenue = Column(Float)
    PaymentMethod = Column(String(255))
    SalesRegion = Column(String(255))

    # Define the relationships
    customer = relationship("Customers", back_populates="sales")
    salesperson = relationship("Users", back_populates="sales")
    product = relationship("Products", back_populates="sales_transaction_details")

class InventoryRecords(db.Base):
    __tablename__ = "Inventory"

    RecordID = Column(Integer, primary_key=True, index=True)
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))  # Establish the Product relationship
    InventoryChangeType = Column(String(255))
    QuantityChange = Column(Integer)
    CurrentInventoryQuantity = Column(Integer)
    InventoryUpdateDateTime = Column(String(255))
    PersonResponsibleID = Column(Integer, ForeignKey('Users.UserID'))  # Establish the PersonResponsible relationship
    Notes = Column(String(255))

    # Define the relationships
    product = relationship("Products", back_populates="inventory_records")
    person_responsible = relationship("Users", back_populates="inventory_records")

class Users(db.Base):
    __tablename__ = "Users"

    UserID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(255))
    PasswordHash = Column(String(255))
    UserRole = Column(String(255))

    # Define the reverse relationship
    sales = relationship("Sales", back_populates="salesperson")
    inventory_records = relationship("InventoryRecords", back_populates="person_responsible")

class ProductCategory(db.Base):
    __tablename__ = "ProductCategory"

    CategoryID = Column(Integer, primary_key=True, index=True)
    CategoryName = Column(String(255))
    CategoryDescription = Column(String(255))

    # Define the reverse relationship
    products = relationship("Products", back_populates="category")

class Manufacturer(db.Base):
    __tablename__ = "Manufacturers"

    ManufacturerID = Column(Integer, primary_key=True, index=True)
    ManufacturerName = Column(String(255))
    ManufacturerDescription = Column(String(255))

    # Define the reverse relationship
    products = relationship("Products", back_populates="manufacturer")

class Customers(db.Base):
    __tablename__ = "Customers"

    CustomerID = Column(Integer, primary_key=True, index=True)
    CustomerName = Column(String(255))
    CustomerContactInfo = Column(String(255))
    CustomerAddress = Column(String(255))

    # Define the reverse relationship
    sales = relationship("Sales", back_populates="customer")

