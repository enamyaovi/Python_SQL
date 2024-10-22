# Introductory Notes
    Hello and welcome to the so called 'easy project' this project is about creating a program that interacts with a database on the mysql server
    using the mysql.connector library and a simple pytho script file to perform some operations. This is like the version 1.0 of the program
    so some things are kinda `CRUDe` get it? Well enough with the puns and the jokes.

    There are three main python files in this package. The main.py file which handles the core logic and the CLI implementation of the program for the user of the
    database to interact with. And two other files namely establish_connection2.py and Inventory_final.py which are modules with one with code about establishing
    the connection to the server and creating a cursor object and the other with a class full of static variables for performing our SQL CRUD operations. 

    The establish_connection2.py file contains a config file with generic server details if you want to experiment with the program on your database you should
    change those details to reflect your credentials for the server connection. Besides that leave everything as is.

    Per the deliverables for this project I am still ways behind. I need to implement export functionality if the data to csv format and write a unit test for the
    scripts. Which I will do maybe 'never' nah just kidding. I'll get to it as soon as possible. 
    You are welcome to try and break this fragile code in anyway that you can. 

    I will also include in this package the skeletons of the program or early versions that show how I was able to come up with the logic and everything.
    It was very interesting to work on so take time and enjoy playing with it. 

    Now I am running out of words to say so here is the end. 
    One last thing is a big shoutout to chat gpt for generating the readme explaining the functionality of my program.
    Documentation is such a pain to be honest and I am glad to be in an era where I can use technological tools for that. Anyways Enjoy

# README for MySQL Connection Script

This script establishes a connection to a MySQL database using the `mysql.connector` library. 
It includes error handling to manage various connection issues.

**Key Components:**

1. **Configuration:**
   - The `config` dictionary holds the credentials for connecting to the MySQL server, including:
     - `user`: The username for the MySQL account.
     - `host`: The hostname of the MySQL server (default is `localhost`).
     - `password`: The password for the MySQL account.

2. **Database and Table Details:**
   - The `shop_details` dictionary contains information about the database and table to be used:
     - `database_name`: Name of the database (`myshop`).
     - `table_name`: Name of the table to interact with (`products`).

3. **Connection and Cursor:**
   - Two variables, `connection` and `mycursor`, are initialized to hold the database connection and cursor objects.

4. **Connecting to the Database:**
   - The script attempts to connect to the MySQL server using the provided configuration. 
   - If the connection is successful, it creates a cursor object to execute SQL queries and prints the server version.

5. **Error Handling:**
   - The script includes specific error handling for common MySQL-related errors:
     - **Access Denied Error:** Triggered if the username or password is incorrect.
     - **Database Does Not Exist Error:** Triggered if the specified database does not exist.
   - It also includes a generic exception handler for unexpected errors.

This script is essential for initializing the connection to the database before performing any database operations. 
Connections to the server are handled closed in the main.py file. 
I couldn't figure out a way to implement closing without running into errors with the cursor not connected.
I will try to figure out better implementation later.

# README for Inventory Management System

This project is an Inventory Management System built using Python and MySQL. 
The system allows users to manage products in a database, including creating the database and tables, inserting data, updating product quantities, deleting
products, viewing inventory, and searching or sorting products. 
It also includes a stock alert feature for products running low on stock. The README contains a simple but clear explaination of 
the methods and logic of the whole package. I used chatgpt to help edit the annotation and craft the documentation. Enjoy!

**Core Components and Logic in `Inventory_final.py`:**

1. **Database Connection and Error Handling**:
   - The `establish_connection2.py` file manages the connection to the MySQL database using `mysql.connector`.
   - If a connection to the database is successfully established, a cursor object (`mycursor`) is created for executing SQL queries.
   - Error handling is done using specific MySQL errors (e.g., `ProgrammingError`, `IntegrityError`, `DatabaseError`)
   -  to ensure that database operations are handled safely and provide feedback if an error occurs.

2. **InventoryManager Class**:
   - This class contains the core functionality for managing the inventory. It uses static methods to interact with the MySQL database.
   - Each method is decorated with `handle_db_errors`, which wraps the function in error handling to catch any issues during database interaction.

3. **Key Methods**:

   - `create_database()`: This method creates the 'myshop' database if it doesn't already exist.
   
   - `connect_database()`: Connects to the 'myshop' database. Once connected, the system can start executing SQL commands on the database.

   - `create_table()`: Creates a `products` table within the 'myshop' database, which stores product details
     such as: `product_id`, `product_name`, `category`, `price`, and `quantity`. If the table already exists, it will not be recreated.

   - `insert_data(data)`: Allows insertion of multiple products into the `products` table.
     The `data` argument should be a list of tuples where each tuple represents a product's information (name, category, price, quantity).

   - `update_quantity(data)`: Updates the quantity of a product based on its `product_id`.
      It accepts a list of dictionaries where each dictionary contains `product_id` and the new `quantity`.

   - `delete_product(product_id)`: Deletes one or more products from the database based on the given product ID(s).
     It can handle both a single ID and a list of IDs.

   - `view_products()`: Fetches and displays all products currently in the `products` table.

   - `search_product(to_search)`: Allows users to search for products based on `product_name` and `category`.
      Wildcards ('%') can be used to search with partial matches.

   - `sort_table(sort_by)`: Sorts and displays products based on the given column.
     By default, it sorts by price, but you can also sort by quantity.

   - `stock_alert()`: This method checks for products with a stock quantity below a defined threshold (5 units) and provides an alert for restocking.

4. **Closing the Database Connection**:
   - The `close()` method ensures that both the cursor and the database connection are closed properly after operations are completed.

The Inventory Management System provides a comprehensive solution to manage a product inventory in a MySQL database, 
ensuring safe and efficient database interactions.
Each feature is encapsulated in well-defined methods that interact with the `products` table and handle any potential database errors gracefully.


# README for main.py
The main.py file serves as the entry point for the Inventory Management System. 
It interacts with the InventoryManager class to perform various inventory-related operations. 
Below is an explanation of its key components and logic.

**Core Logic in `main.py`:**

- Menu Display:

    The script begins by displaying a menu with various inventory management options like
      creating a database, creating a table, adding products, updating quantities, viewing products, and more.

  Helper Functions:
    get_positive_integer(prompt): Ensures user input for quantities or IDs is a non-negative integer.
    get_positive_float(prompt): Ensures user input for prices is a non-negative float.

**Main Functionality:**

    The main() function runs in a loop and continuously prompts the user to select an option from the menu (1-10).
    Depending on the user's choice, it triggers corresponding methods from the InventoryManager class to manage inventory operations.
    Options:

    Create Database: Initializes a new database for inventory management.
    Create Table: Creates a products table with fields like product name, category, price, and quantity.
    Add Product: Collects product details from the user and inserts them into the table.
    Update Product Quantity: Updates the quantity of a product based on the product ID.
    Delete Product: Deletes a product from the table using its ID.
    View Products: Displays all products in the inventory.
    Search Product: Allows searching for products by name or category.
    Sort Products: Sorts the product list by price or quantity.
    Stock Alert: Alerts the user if any product has a low stock (quantity below 5).
    Exit: Closes the database connection and exits the program.
    Error Handling:

The script includes basic error handling to capture any issues during execution and provide user-friendly messages.
This file is designed to provide a user-friendly interface for managing an inventory database through command-line inputs.# README FOR MAIN.py

