INSERT INTO TestApplication.Customers
(CustomerID, CustomerName, CustomerContactInfo, CustomerAddress)
VALUES(1, 'Customer1', 'customer1@gmail.com', 'Street2, West, Pk');

INSERT INTO TestApplication.Manufacturers
(ManufacturerID, ManufacturerName, ManufacturerDescription)
VALUES(1, 'Nestle', 'Eatable goods');

INSERT INTO TestApplication.Users
(UserID, Username, PasswordHash, UserRole)
VALUES(1, 'Employee001', '123', 'Manager');

INSERT INTO TestApplication.ProductCategory
(CategoryID, CategoryName, CategoryDescription)
VALUES(1, 'Eatables', 'Chips, chocolate, milk');

INSERT INTO TestApplication.Products
(ProductID, ProductName, ProductDescription, ProductCategoryID, ProductPrice, ManufacturerID, CurrentInventoryQuantity, LowStockThreshold, DateAddedToInventory, ProductImage)
VALUES(1, 'Chocobar', 'Dark Chocolate', 1, 30, 1, 150, 160, '2023-10-01T18:41:42.676', 'pic.png');

INSERT INTO TestApplication.Sales
(SalesID, SaleDateTime, CustomerID, SalespersonID, ProductID, QuantitySold, TotalRevenue, PaymentMethod, SalesRegion)
VALUES(1, '2023-10-01T18:41:42.676', 1, 1, 1, 200, 6000, 'credit card', 'north');

INSERT INTO TestApplication.Inventory
(RecordID, ProductID, InventoryChangeType, QuantityChange, CurrentInventoryQuantity, InventoryUpdateDateTime, PersonResponsibleID, Notes)
VALUES(1, 1, 'sale', 10,150, '2023-10-01T18:41:42.676', 1, 'Urgent need');
