from shopping import Product, Clothing, Food, ShoppingCart

# Create a ShoppingCart
shopping_cart = ShoppingCart()

if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    
    print('The program has started.')
    print('Insert your next command (H for help):')
    terminated = False
    
    while not terminated:
        command = input("Type your next command: ").strip().upper()
    
        if command == 'A':
            # Add a product to the cart
            print("Adding new product")
            
            product_type = input("Insert its type:")
            if product_type not in ['Clothing', 'Food']:
                print("Invalid product type. Please try again.")
            else:
                name = input("Insert its name: ")
                price = float(input("Insert its price (£): "))
                quantity = int(input("Insert its quantity: "))
                brand = input("Insert its brand: ")
    
            
            
                if product_type == 'Clothing':
                    size = input("Insert its size: ")
                    material = input("Insert its material: ")
                    product = Clothing(name, price, quantity, brand, size, material)
                elif product_type == 'Food':
                    expiry_date = input("Insert its expiry date(YYYY-MM-DD): ")
                    gluten_free = input("Is it gluten-free? (True/False): ").strip().lower() == 'true'
                    suitable_for_vegans = input("Is it suitable for vegans? (True/False): ").strip().lower() == 'true'
                    product = Food(name, price, quantity, brand, expiry_date, gluten_free, suitable_for_vegans)
    
                shopping_cart.addProduct(product)
                print(f"The product {product.name} has been added to the cart.")
    
        elif command == 'R':
            # Remove a product from the cart
            name = input("Enter product name to remove: ")
            matching_products = [product for product in shopping_cart.cart if product.name == name]
            if matching_products:
                shopping_cart.removeProduct(matching_products[0])
                print(f"{name} has been removed from the cart.")
            else:
                print(f"No product named '{name}' found in the cart. No removal took place.")
    
        elif command == 'S':
        # Print a summary of the cart
            cart_contents = shopping_cart.getContents()
            total_cost = 0
            if not cart_contents:
                print("The cart is empty.")
            else:               
                i = 1
                print("Cart Contents:")
            for product in cart_contents:
                cost = product.price * product.quantity
                total_cost += cost
                if product.quantity != 1:
                    print(f"{i} - {product.quantity} * {product.name}  = £{cost:.2f}")
                else:
                    print(f"{i} - {product.name}  = £{cost:.2f}")
                i = i+1
            print(f"Total Cost: ${total_cost:.2f}")
    
        elif command == 'Q':
            # Change the quantity of a product
            name = input("Enter product name to change quantity: ")
            quantity = int(input("Enter the new quantity: "))
            matching_products = [product for product in shopping_cart.cart if product.name == name]
            if matching_products:
                shopping_cart.changeProductQuantity(matching_products[0], quantity)
                print(f"Quantity of {name} has been changed to {quantity}.")
            else:
                print(f"No product named '{name}' found in the cart. No changes took place.")
    
        elif command == 'E':
            # Export the cart contents to JSON
            cart_json = shopping_cart.to_json()
            print("Cart Contents (JSON format):")
            print(cart_json)
    
        elif command == 'T':
            # Terminate the program
            terminated = True
    
        elif command == 'H':
            # Help - Print the list of available commands
            print("Available commands:")
            print("A - Add a product to the cart")
            print("R - Remove a product from the cart")
            print("S - Print a summary of the cart")
            print("Q - Change the quantity of a product")
            print("E - Export the cart contents to JSON")
            print("T - Terminate the program")
            print("H - Display available commands")
    
        else:
            print("Command not recognized. Please try again.")
    
    print('Goodbye.')