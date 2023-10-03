##### Database

### Products Table
- This table stores information about products.
- **Columns:**
  - **ProductID (Primary Key):** An identifier for each product.
  - **ProductName:** The name of the product.
  - **ProductDescription:** A description of the product.
  - **ProductCategoryID (Foreign Key):** Links to the ProductCategory table, indicating the category to which the product belongs.
  - **ProductPrice:** The price of the product.
  - **ManufacturerID (Foreign Key):** Links to the Manufacturers table, specifying the manufacturer of the product.
  - **CurrentInventoryQuantity:** The current quantity of the product in stock.
  - **LowStockThreshold:** A threshold quantity indicating when the product is considered to be in low stock.
  - **DateAddedToInventory:** The date when the product was added to the inventory.
  - **ProductImage:** A reference to an image of the product.

- **Relationships:**
  - **Category:** Relates to the ProductCategory table to specify the product's category.
  - **Manufacturer:** Relates to the Manufacturers table to specify the product's manufacturer.
  - **Inventory Records:** Links to the InventoryRecords table to track changes in inventory for this product.
  - **Sales Transaction Details:** Links to the Sales table to track sales transactions involving this product.

### Sales Table
- This table records sales transactions.
- **Columns:**
  - **SalesID (Primary Key):** An identifier for each sales transaction.
  - **SaleDateTime:** The date and time of the sale.
  - **CustomerID (Foreign Key):** Links to the Customers table, specifying the customer who made the purchase.
  - **SalespersonID (Foreign Key):** Links to the Users table, indicating the salesperson responsible for the sale.
  - **ProductID (Foreign Key):** Links to the Products table, identifying the product sold.
  - **QuantitySold:** The quantity of the product sold in the transaction.
  - **TotalRevenue:** The total revenue generated from the sale.
  - **PaymentMethod:** The payment method used for the transaction.
  - **SalesRegion:** The region where the sale occurred.

- **Relationships:**
  - **Customer:** Relates to the Customers table to specify the customer who made the purchase.
  - **Salesperson:** Relates to the Users table to specify the salesperson responsible for the sale.
  - **Product:** Relates to the Products table to specify the product sold.

### InventoryRecords Table
- This table records changes in inventory levels over time.
- **Columns:**
  - **RecordID (Primary Key):** An identifier for each inventory record.
  - **ProductID (Foreign Key):** Links to the Products table, specifying the product affected by the inventory change.
  - **InventoryChangeType:** Describes the type of inventory change (e.g., restock, sale).
  - **QuantityChange:** The quantity by which the inventory changed (positive for additions, negative for subtractions).
  - **CurrentInventoryQuantity:** The current quantity of the product in stock after the change.
  - **InventoryUpdateDateTime:** The date and time when the inventory change occurred.
  - **PersonResponsibleID (Foreign Key):** Links to the Users table, indicating the person responsible for the inventory change.
  - **Notes:** Optional comments related to the inventory change.

- **Relationships:**
  - **Product:** Relates to the Products table to specify the product affected by the inventory change.
  - **Person Responsible:** Relates to the Users table to specify the person responsible for the inventory change.

### Users Table
- This table stores information about users, including sales people and personnel responsible for inventory management.
- **Columns:**
  - **UserID (Primary Key):** An identifier for each user.
  - **Username:** The username of the user.
  - **PasswordHash:** The hashed password of the user.
  - **UserRole:** Specifies the role of the user (e.g., salesperson, inventory manager).

- **Relationships:**
  - **Sales:** Relates to the Sales table to track sales transactions associated with this user.
  - **Inventory Records:** Relates to the InventoryRecords table to track inventory changes made by this user.

### ProductCategory Table
- This table defines product categories.
- **Columns:**
  - **CategoryID (Primary Key):** An identifier for each product category.
  - **CategoryName:** The name of the product category.
  - **CategoryDescription:** A description of the product category.

- **Relationships:**
  - **Products:** Relates to the Products table to categorize products into specific categories.

### Manufacturer Table
- This table stores information about product manufacturers.
- **Columns:**
  - **ManufacturerID (Primary Key):** An identifier for each manufacturer.
  - **ManufacturerName:** The name of the manufacturer.
  - **ManufacturerDescription:** A description of the manufacturer.

- **Relationships:**
  - **Products:** Relates to the Products table to specify the manufacturer of products.

### Customers Table
- This table stores information about customers who make purchases.
- **Columns:**
  - **CustomerID (Primary Key):** An identifier for each customer.
  - **CustomerName:** The name of the customer.
  - **CustomerContactInfo:** Contact information for the customer.
  - **CustomerAddress:** The address of the customer.

- **Relationships:**
  - **Sales:** Relates to the Sales table to track sales transactions associated with specific customers.

This database schema is designed to efficiently manage and track products, sales, inventory changes, users, product categories, manufacturers, and customers within the e-commerce application while maintaining data integrity through appropriate relationships and constraints.