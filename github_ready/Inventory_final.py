from establish_connection import connection, mycursor
from mysql.connector import errors as MySQL_Error
from functools import wraps

class InventoryManager:
    """
    A class to manage the inventory operations such as creating a database, 
    inserting data, updating product details, and handling database errors.
    """

    def handle_db_errors(func):
        """
        Decorator function to handle database-related exceptions.
        
        Args:
            func: The function being wrapped by the decorator.
        
        Returns:
            Wrapper function that executes the original function and catches any 
            database errors, printing appropriate messages.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Database error occurred: {e}")
                return False
            except MySQL_Error.ProgrammingError as e:
                # Raised if there is a syntax error in the SQL query
                print("Programming error: Issue with SQL syntax.")
                print(f"Details: {e}")
                return False
            except MySQL_Error.DatabaseError as e:
                # Raised for issues related to the database connection or operation
                print("Database error: Problem occurred while creating the database.")
                print(f"Details: {e}")
                return False
            except MySQL_Error.IntegrityError as e:
                # Raised when data violates integrity constraints (e.g., duplicate entries, foreign key issues)
                print("Integrity error: Data conflicts with existing constraints.")
                print(f"Details: {e}")
                return False
        return wrapper

    @staticmethod
    @handle_db_errors 
    def create_database() -> bool:
        """
        Creates the 'myshop' database if it does not already exist.

        Returns:
            bool: True if the database was created successfully, otherwise False.
        """
        mycursor.execute("CREATE DATABASE IF NOT EXISTS myshop;")
        print("Database created or already exists. Database name: myshop")
        return True

    @staticmethod
    @handle_db_errors
    def connect_database() -> bool:
        """
        Connects to the 'myshop' database and sets it for use.

        Returns:
            bool: True if the database was successfully connected to, otherwise False.
        """
        mycursor.execute('USE myshop;')
        print('Using the database, "myshop"')
        return True

    @staticmethod
    @handle_db_errors
    def create_table() -> bool:
        """
        Creates the 'products' table in the 'myshop' database if it does not already exist.

        Returns:
            bool: True if the table was created successfully, otherwise False.
        """
        mycursor.execute('USE myshop;')
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(255) UNIQUE,
                category VARCHAR(255),
                price FLOAT,
                quantity INT
            );
        """)
        print("Table created or already exists. Table name: products")
        
        return True

    @staticmethod
    @handle_db_errors
    def insert_data(data: list[tuple]) -> bool:
        """
        Inserts multiple records into the 'products' table in the 'myshop' database.

        Args:
            data (list[tuple]): A list of tuples, where each tuple represents a row to be inserted.
                                Each tuple should contain (product_name: str, category: str, price: float, quantity: int).
                                The order and data types should be respected to avoid errors. 

        Returns:
            bool: True if the data was inserted successfully, otherwise False.
        """
        insert_query = """
            INSERT INTO products (product_name, category, price, quantity)
            VALUES (%s, %s, %s, %s);
        """
        mycursor.executemany(insert_query, data)  # Insert multiple rows at once
        connection.commit()  # Commit the changes to the database
        for element in data:
            print(f"Product {element} added.")
        return True

    @staticmethod
    @handle_db_errors
    def update_quantity(data: list[dict[str, int]]) -> bool:
        """
        Updates the quantity of products in the 'products' table based on the product ID.

        Args:
            data (list[dict[str, int]]): A list of dictionaries where each dictionary contains 
                                         'quantity' and 'product_id'. Each dictionary should have the format:
                                         {"quantity": int, "product_id": int}.

        Returns:
            bool: True if the update was successful, otherwise False.
        """
        update_query = "UPDATE products SET quantity = %(quantity)s WHERE product_id = %(product_id)s;"
        mycursor.executemany(update_query, data)  # Updates multiple products at once
        connection.commit()  # Commit the transaction
        print(f"{mycursor.rowcount} row(s) updated.")  # Prints the number of rows updated
        return True

    @staticmethod
    @handle_db_errors
    def delete_product(product_id: list[int] | int) -> bool:
        """
        Deletes one or more products from the 'products' table based on the provided product ID(s).

        Args:
            product_id (list[int] | int): A list of product IDs or a single product ID representing
                                          the products to be deleted.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        delete_query = "DELETE FROM products WHERE product_id = %s;"
        if isinstance(product_id, int):
            product_id = [(product_id,)]  # Convert single product ID to tuple format
        else:
            product_id = [(pid,) for pid in product_id]  # Ensure list of IDs is in tuple format
        mycursor.executemany(delete_query, product_id)  # Deletes multiple products at once
        connection.commit()  # Commit the transaction
        print(f"{mycursor.rowcount} row(s) deleted.")  # Prints the number of rows deleted
        return True

    @staticmethod
    @handle_db_errors
    def view_products() -> None:
        """
        Retrieves and displays all products from the 'products' table.

        This method executes a SQL query to select all entries from the 'products' table
        and prints the details of each product.

        Returns:
            None
        """
        mycursor.execute("SELECT * FROM products;")  # Select all products
        result = mycursor.fetchall()  # Fetch all results
        for row in result:
            print(row)  # Prints each product row

    @staticmethod
    @handle_db_errors
    def search_product(to_search: dict[str, str] = {'product_name': '%', 'category': '%'}) -> None:
        """
        Searches for products in the 'products' table based on the provided criteria.

        Args:
            to_search (dict[str, str]): A dictionary containing search criteria with keys 
                                        'product_name' and/or 'category'. Use the wild card '%'
                                        to search with partial matches or for any value.
                                        Default search is set to all products unless specified.

        Returns:
            None
        """
        sql = "SELECT * FROM products WHERE product_name LIKE %(product_name)s AND category LIKE %(category)s;"
        mycursor.execute(sql, to_search)  # Executes the search query with given criteria
        result = mycursor.fetchall()  # Fetch all matching results
        if result:
            for row in result:
                print(row)  # Prints each matching product row
        else:
            print('Nothing Found :(')  # Print if no products were found

    @staticmethod
    @handle_db_errors
    def sort_table(sort_by: str = "price") -> None:
        """
        Retrieves and displays all products from the 'products' table, sorted by the specified column.

        Args:
            sort_by (str): The column to sort the products by. Defaults to "price".
                           Acceptable values are "price" or "quantity".

        Returns:
            None
        """
        allowed_sort_columns = ["price", "quantity"]  # List of allowed sorting columns
        if sort_by not in allowed_sort_columns:
            print("Invalid sort parameter.")  # Handle invalid sort option
            return
        mycursor.execute(f"SELECT * FROM products ORDER BY {sort_by};")  # Sort by the selected column
        result = mycursor.fetchall()  # Fetch all sorted results
        for row in result:
            print(row)  # Prints each product row sorted by the selected column

    @staticmethod
    @handle_db_errors
    def stock_alert() -> None:
        """
        Checks for products with stock levels below the defined threshold and alerts for restocking.

        The method executes a SQL query to select all products from the 'products' table
        where the quantity is less than 5 and displays those products for restocking alerts.

        Returns:
            None
        """
        mycursor.execute("SELECT * FROM products WHERE quantity < 5;")  # Select products with low stock
        result = mycursor.fetchall()  # Fetch all matching results
        if not result:
            print("No products need restocking.")  # Print if no products need restocking
        else:
            for row in result:
                print(f"Restock {row[1]} - Current stock: {row[4]}")  # Print products that need restocking

    def close(*args, **kwargs):
        """
        Closes the cursor and connection to the database.

        This function checks if the cursor and connection are still open, and closes them if necessary.
        """
        if mycursor and not mycursor.close:
            mycursor.close()  # Close the cursor if it hasn't been closed yet
        if connection.is_connected():
            connection.close()  # Close the database connection
            print('Connection to Database and Server Closed!')
