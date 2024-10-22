import mysql.connector
import mysql.connector.errors as err
import mysql.connector.errorcode

# Configuration for connecting to the MySQL server
config = {
    'user': 'root',
    'host': 'localhost',
    'password': 'somepassword'
}

# Details about the database and table to be used
shop_details = {
    'database_name': 'myshop',
    'table_name': 'products'
}

# Variables to hold the connection and cursor objects
connection = None
mycursor = None

# Establishing connection to the Database Server and creating a cursor
try:
    # Attempt to connect to the MySQL server using the provided configuration
    connection = mysql.connector.connect(**config)

    # Check if the connection is established and the server is reachable
    if connection and connection.is_connected():
        # Create a cursor object for executing queries
        mycursor = connection.cursor()
        print(mycursor, connection.get_server_version())  # Output the cursor object to confirm it's created
    else:
        # If the connection isn't established, provide an appropriate message
        print('Something went wrong with the connection.')

# Exception handling for different types of MySQL-related errors
except err as e:
    print(f"Details: {e}")
except Exception as e:
    # Generic exception for unexpected errors not related to MySQL
    print("An unexpected error occurred. Please check the details.")
    print(f"Details: {e}")