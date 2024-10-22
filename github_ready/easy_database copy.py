import mysql.connector
import mysql.connector.cursor
import mysql.connector.errors as cnx_err
# from rawscript import config



config = {
        'user':'root',
        'host':'localhost',
        'password':'somepassword'
            }


connection = None
mycursor = None
try:
    connection = mysql.connector.connect(**config) 
    if connection and connection.is_connected():
        mycursor = connection.cursor()
        print(mycursor)

    else:
        print('Execute Connection Error')
except mysql.connector.Error as err:
    print(err)
except BaseException as err:
    print(f'Something went wrong :( \n{err}')


# CREATING THE DATABASE
mycursor.execute('CREATE DATABASE IF NOT EXISTS myShop;')

# CREATING THE TABLE

mycursor.execute("""
    USE DATABASE myShop;
        CREATE TABLE IF NOT EXISITS products
                 (
                    product_id INT AUTO_INCREMENT PRIMARY KEY,
                    product_name VARCHAR(255) NOT NULL UNIQUE,
                    price FLOAT(6,2) NOT NULL,
                    quantity INT,
                    category VARCHAR(255)
                 );""", multi=True)

#INSERTING DATA INTO THE TABLE and saving operation
mycursor.execute("""
    INSERT INTO products 
                 (product_name, price, quantity, category)
                    VALUES  (),
                            ()
                            ();""")
connection.commit()

#VIEW ALL PRODUCTS IN THE TABLE
mycursor.execute("""
    SELECT *
        FROM products; """)
result = mycursor.fetchall()
print('PRODUCTS: ')
for row in result:
    print(row)

#UPDATE PRODUCT DETAILS
sql = """
    UPDATE products
        SET product_name = %(product_name)s, price = %(price)s, category = %(category)s
                 WHERE product_id = %(product_id)s;"""
data = {
    'product_name': '',
    'price':'',
    'category':'',
    'product_id':''}
mycursor.execute(sql, data)
result = mycursor.fetchall()
for row in result:
    print(row)
connection.commit()

#update stock of product quantity
sql = """"
    UPDATE products
        SET quantity = %(quantity)s
            WHERE product_id = %(product_id)s;
            """
data = {'quantity': '', 'product_id': ''}
mycursor.execute(sql, data)
result = mycursor.fetchall()
for row in result:
    print(row)
connection.commit()

#Delete a product
sql = """
    DELETE FROM products
        WHERE product_id = %(product_id)s;"""
data = {'product_id': ''}
mycursor.execute(sql, data)
result = mycursor.fetchall()
for row in result:
    print(row)
connection.commit()

#Low Stock ALert
sql = """
    SELECT *
        FROM products
            WHERE quantity < 5 ;"""
mycursor.execute(sql)
result = mycursor.fetchall()
for row in result:
    print(f'Restock: {row[1]}. Current stock: {row[3]}')

#search products by name or category
sql = """
    SELECT * 
        FROM products
            WHERE product_name = %(product_name)s OR category = %(category)s;"""
data = {'product_name':'', 'category':''}
mycursor.execute(sql, data.values())
result = mycursor.fetchall()
for row in result:
    print(row)

#sort by price or quantity
sql ="""
    SELECT *
        FROM products
            ORDER BY %s OR %s;"""
data = ('price', 'quantity')
mycursor.execute(sql, data)
result = mycursor.fetchall()
for row in result:
    print(row)


