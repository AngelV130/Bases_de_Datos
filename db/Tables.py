# Crear Objeto de cada tabla de la base de datos

Order_Details = {
    "name": "`Order Details`",
    "columns": ["OrderID","ProductID","UnitPrice","Quantity","Discount"]
}
Categories = {
    "name": "Categories",
    "columns": ["CategoryID", "CategoryName", "Description"]
}
CustomerCustomerDemo = {
    "name": "CustomerCustomerDemo",
    "columns": ["CustomerID", "CustomerTypeID"]
}
CustomerDemographics = {
    "name": "CustomerDemographics",
    "columns": ["CustomerTypeID", "CustomerDesc"]
}
Customers = {
    "name": "Customers",
    "columns": ["CustomerID", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax"]
}
Employees = {
    "name": "Employees",
    "columns": ["EmployeeID", "LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Notes", "ReportsTo", "PhotoPath", "Salary"]
}
EmployeeTerritories = {
    "name": "EmployeeTerritories",
    "columns": ["EmployeeID", "TerritoryID"]
}
Orders = {
    "name": "Orders",
    "columns": ["OrderID", "CustomerID", "EmployeeID", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry"]
}
Products = {
    "name": "Products",
    "columns": ["ProductID", "ProductName", "SupplierID", "CategoryID", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued"]
}
Region = {
    "name": "Region",
    "columns": ["RegionID", "RegionDescription"]
}
Shippers = {
    "name": "Shippers",
    "columns": ["ShipperID", "CompanyName", "Phone"]
}
Suppliers = {
    "name": "Suppliers",
    "columns": ["SupplierID", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage"]
}
Territories = {
    "name": "Territories",
    "columns": ["TerritoryID", "TerritoryDescription", "RegionID"]
}









    #Query's de todas las tablas
    # pandas = Pandas('resources/xlsx', 'Order_Details.xlsx')
    # # 1. Order Details
    # order_details_columns = ', '.join(Order_Details["columns"])
    # order_details_name = Order_Details["name"]
    # order_details_query = f"SELECT {order_details_columns} FROM {order_details_name} LIMIT 12"
    # customers = connection.execute_query(order_details_query)
    # df = pandas.build(customers, Order_Details['columns'])
    # print(df)
    # # 2. Categories
    # categories_columns = ', '.join(Categories["columns"])
    # categories_name = Categories["name"]
    # categories_query = f"SELECT {categories_columns} FROM {categories_name} LIMIT 12"
    # customers = connection.execute_query(categories_query)
    # df = pandas.build(customers, Categories['columns'])
    # print(df)
    # # 5. Customers
    # customers_columns = ', '.join(Customers["columns"])
    # customers_name = Customers["name"]
    # customers_query = f"SELECT {customers_columns} FROM {customers_name} LIMIT 12"
    # customers = connection.execute_query(customers_query)
    # df = pandas.build(customers, Customers['columns'])
    # print(df)
    # # 6. Employees
    # employees_columns = ', '.join(Employees["columns"])
    # employees_name = Employees["name"]
    # employees_query = f"SELECT {employees_columns} FROM {employees_name} LIMIT 12"
    # customers = connection.execute_query(employees_query)
    # df = pandas.build(customers, Employees['columns'])
    # print(df)
    # # 8. Orders
    # orders_columns = ', '.join(Orders["columns"])
    # orders_name = Orders["name"]
    # orders_query = f"SELECT {orders_columns} FROM {orders_name} LIMIT 12"
    # customers = connection.execute_query(orders_query)
    # df = pandas.build(customers, Orders['columns'])
    # print(df)
    # # 9. Products
    # products_columns = ', '.join(Products["columns"])
    # products_name = Products["name"]
    # products_query = f"SELECT {products_columns} FROM {products_name} LIMIT 12"
    # customers = connection.execute_query(products_query)
    # df = pandas.build(customers, Products['columns'])
    # print(df)
    # # 10. Region
    # region_columns = ', '.join(Region["columns"])
    # region_name = Region["name"]
    # region_query = f"SELECT {region_columns} FROM {region_name} LIMIT 12"
    # customers = connection.execute_query(region_query)
    # df = pandas.build(customers, Region['columns'])
    # print(df)
    # # 11. Shippers
    # shippers_columns = ', '.join(Shippers["columns"])
    # shippers_name = Shippers["name"]
    # shippers_query = f"SELECT {shippers_columns} FROM {shippers_name} LIMIT 12"
    # customers = connection.execute_query(shippers_query)
    # df = pandas.build(customers, Shippers['columns'])
    # print(df)
    # # 12. Suppliers
    # suppliers_columns = ', '.join(Suppliers["columns"])
    # suppliers_name = Suppliers["name"]
    # suppliers_query = f"SELECT {suppliers_columns} FROM {suppliers_name} LIMIT 12"
    # customers = connection.execute_query(suppliers_query)
    # df = pandas.build(customers, Suppliers['columns'])
    # print(df)
    # # 13. Territories
    # territories_columns = ', '.join(Territories["columns"])
    # territories_name = Territories["name"]
    # territories_query = f"SELECT {territories_columns} FROM {territories_name} LIMIT 12"
    # customers = connection.execute_query(territories_query)
    # df = pandas.build(customers, Territories['columns'])
    # print(df)