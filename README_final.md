# Introductory Notes

Welcome to the *'easy project'* (I say easy, but we both know it's a journey)! 
This project is all about creating a Python program that interacts with a MySQL database using the `mysql.connector` library. 
It’s version 1.0, so, yes, some things are still a bit "CRUDe" (see what I did there?). Enough jokes, let's get to it!

In this package, you'll find three Python files:
- `main.py`: This is the heart of the program, handling core logic and the CLI for user interaction with the database.
- `establish_connection2.py`: A module for setting up the MySQL connection.
- `Inventory_final.py`: A class packed with static methods for managing our SQL CRUD operations.

You can experiment with the program by tweaking the credentials in `establish_connection2.py`—
just update the config file with your MySQL server details. Otherwise, everything should be good to go!

As for the deliverables... I’m still a bit behind (shocking, I know). 
I need to add an export to CSV feature and write some unit tests. I promise I’ll get to it... eventually.

Feel free to break this fragile code—I’ll take it as constructive chaos! 
Also, check out the earlier versions included in the package to see how the logic evolved. 
It’s been a fun project, and I hope you enjoy playing around with it.

Oh, and a big shoutout to ChatGPT for helping me with this README. 
Documenting code is *hard*, but with a little help, it's not so bad. Enjoy!

---

# README for MySQL Connection Script

This script establishes a connection to a MySQL database using the `mysql.connector` library and includes basic error handling.

### Key Components:

1. **Configuration**:  
   The `config` dictionary contains:
   - `user`: Your MySQL username.
   - `host`: The MySQL server (default is `localhost`).
   - `password`: Your MySQL password.

2. **Database and Table Info**:  
   The `shop_details` dictionary has:
   - `database_name`: Name of the database (`myshop`).
   - `table_name`: Name of the table (`products`).

3. **Connection and Cursor**:  
   Variables `connection` and `mycursor` hold the database connection and cursor for SQL operations.

4. **Error Handling**:  
   Specific error handling for:
   - Access Denied (wrong credentials).
   - Database not found.
   And general handling for other errors.

The `main.py` file handles closing the connection. I’m still working on a smooth way to close it without cursor errors!

---

# README for Inventory Management System

This project is an Inventory Management System built with Python and MySQL. 
You can manage products in a database, including adding, updating, deleting, and viewing products, plus a handy stock alert for low inventory.

### Key Features:

- **Database Connection**:  
  Managed in `establish_connection2.py`, it connects to the MySQL database and creates a cursor for SQL queries.

- **InventoryManager Class**:  
  Contains methods for all database operations like creating a database, adding products, updating quantities, and more.

- **Methods in `Inventory_final.py`**:
  - `create_database()`: Sets up the database.
  - `create_table()`: Creates a `products` table.
  - `insert_data()`: Adds products.
  - `update_quantity()`: Updates stock.
  - `delete_product()`: Removes products by ID.
  - `view_products()`: Displays all products.
  - `search_product()`: Search by name or category.
  - `sort_table()`: Sorts products (by price or quantity).
  - `stock_alert()`: Alerts you for low stock.

- **Closing the Connection**:  
  The `close()` method ensures the cursor and connection are properly closed after operations.

---

# README for main.py

`main.py` is the entry point of the Inventory Management System, providing a simple command-line interface for managing inventory.

### Main Features:

- **Menu Options**:  
  Displays a menu with options like creating a database, adding products, updating stock, deleting products, and more.

- **Helper Functions**:  
  - `get_positive_integer()`: Ensures input is a valid integer.
  - `get_positive_float()`: Ensures input is a valid float.

- **Core Operations**:  
  Based on the user’s menu selection, the program calls methods from `InventoryManager` to handle tasks like:
  - Creating a database and table.
  - Adding and updating products.
  - Viewing and sorting inventory.
  - Stock alerts for low quantities.

- **Error Handling**:  
  The script includes basic error handling for smooth user experience.

This file is designed to make managing your inventory easy through simple command-line inputs.

# BUGS IN CURRENT IMPLEMENTATION
  To be updated...

# CHALLENGES FACED
  To be updated...