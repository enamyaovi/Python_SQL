from Inventory_final import InventoryManager

def display_menu():
    """
    Displays the inventory management menu with available options.
    """
    print("\n=== Inventory Management Menu ===")
    print("1. Connect to Database")
    print("2. Create Table")
    print("3. Add Product")
    print("4. Update Product Quantity")
    print("5. Delete Product")
    print("6. View Products")
    print("7. Search Product")
    print("8. Sort Products")
    print("9. Stock Alert")
    print("10. Exit \n")


def get_positive_integer(prompt):
    """
    Prompts the user for a non-negative integer input. 
    Ensures valid input by handling exceptions.
    
    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        int: A valid non-negative integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_positive_float(prompt):
    """
    Prompts the user for a non-negative float input. 
    Ensures valid input by handling exceptions.
    
    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        float: A valid non-negative float input from the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative price.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """
    Main function to run the Inventory Management System. 
    Provides an interactive menu for managing products in a database.
    """
    # Establish connection to the database
    if not InventoryManager.connect_database():
        return

    # Create an instance of InventoryManager to manage the inventory
    manager = InventoryManager()

    # Loop to display the menu and process user inputs
    while True:
        display_menu()  # Show the menu options

        try:
            # Prompt the user for menu choice
            choice = input("Select an option (1-10): ")

            # Option 1: Connect to Database
            if choice == "1":
                manager.connect_database()

            # Option 2: Create Table
            elif choice == "2":
                manager.create_table()
                

            # Option 3: Add Product
            elif choice == "3":
                product = {
                    "product_name": input("Product Name: "),
                    "category": input("Category: "),
                    "price": get_positive_float("Price: "),
                    "quantity": get_positive_integer("Quantity: ")
                }
                # Convert product details to a tuple and add to the product list
                pro = tuple(product.values())
                products = [pro]
                manager.insert_data(products)

            # Option 4: Update Product Quantity
            elif choice == "4":
                product_id = get_positive_integer("Product ID: ")
                quantity = get_positive_integer("New Quantity: ")
                manager.update_quantity([{"product_id": product_id, "quantity": quantity}])

            # Option 5: Delete Product
            elif choice == "5":
                product_id = get_positive_integer("Product ID to delete: ")
                confirm = input(f"Are you sure you want to delete product ID {product_id}? (y/n): ")
                if confirm.lower() == 'y':
                    manager.delete_product(product_id)

            # Option 6: View Products
            elif choice == "6":
                manager.view_products()

            # Option 7: Search Product
            elif choice == "7":
                search_criteria = {
                    "product_name": input("Product Name to search (or press Enter): ") + '%',
                    "category": input("Category to search (or press Enter): ") + '%'
                }
                # Search using the given criteria
                manager.search_product(search_criteria)

            # Option 8: Sort Products
            elif choice == "8":
                sort_by = input("Select sorting parameter (price/quantity): ").lower().strip()
                if sort_by not in ['price', 'quantity']:
                    print("Invalid parameter. Defaulting to 'price'.")
                    sort_by = 'price'
                manager.sort_table(sort_by)

            # Option 9: Stock Alert
            elif choice == "9":
                manager.stock_alert()

            # Option 10: Exit the program
            elif choice == "10":
                print("Exiting...")
                manager.close()  # Close the database connection
                break

            # Invalid option handling
            else:
                print("Invalid option. Please try again.")

        # Handle unexpected errors during execution
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


# Entry point for the script
if __name__ == "__main__":
    main()
