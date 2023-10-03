# E-Commerce Admin Dashboard

The **E-Commerce Admin Dashboard** is a web application built using FastAPI and Python. It provides e-commerce managers with detailed insights into sales, revenue, and inventory status, along with the ability to register new products and more. This README file serves as a guide to understand, set up, and use the application effectively.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Features

- **Sales Status:**
  - Endpoints to retrieve, filter, and analyze sales data.
  - Endpoints to analyze revenue on a daily, weekly, monthly, and annual basis.
  - Ability to compare revenue across different time periods and categories.
  - Provide sales data by date range, product, and category.

- **Inventory Management:**
  - Endpoints to view current inventory status.
  - Low stock alerts to manage inventory levels effectively.
  - Functionality to update inventory levels and track changes over time.

## Installation

Follow these steps to set up and run the E-Commerce Admin Dashboard on your local development environment:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/e-commerce-admin-dashboard.git
   cd e-commerce-admin-dashboard

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt

4. Configure your environment variables by creating a .env file in the project root directory. You need to set database connection details().

5. Start the FastAPI application:
   
   ```bash
   uvicorn app.main:app --reload

The E-Commerce Admin Dashboard should now be accessible at http://localhost:8000.
Usage

### Dashboard

Here you can access the following features:

   1. Navigate to the sales dashboard to retrieve, filter, and analyze sales data. Use the provided filters to view sales by date range, product, and category.

   2. Access the revenue analysis section to view revenue data on a daily, weekly, monthly, and annual basis. Compare revenue across different time periods and categories.

   3. Manage your inventory by viewing current status and receiving low stock alerts. Update inventory levels and track changes over time.
   
   4. Register new products by providing product details, including name, description, price, and category. Use the /product/register endpoint to add new products to your inventory.

### API Documentation

For detailed API documentation and endpoint descriptions, refer to the API documentation page accessible at /docs or /redoc when running the application.
Dependencies

The project relies on several Python libraries and tools, including but not limited to:

    * FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
    * SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
    * Uvicorn: ASGI server for running FastAPI applications.

Please refer to the requirements.txt file for a full list of dependencies and versions used in this project.