from shopping import Product, Clothing, Food, ShoppingCart

# Create Product instances
product1 = Clothing("Shirt", 19.99, 3, "Nike", "Medium", "Cotton")
product2 = Food("Chocolate", 5.99, 2, "Hershey's", "2023-12-31", True, True)
product3 = Food("Biscuit", 9.99, 1, "Digestive", "2023-12-12", True, True)

# Create a ShoppingCart
shopping_cart = ShoppingCart()

# Test adding products to the cart
shopping_cart.addProduct(product1)
shopping_cart.addProduct(product2)
shopping_cart.addProduct(product3)

# Test changing product quantity
shopping_cart.changeProductQuantity(product1, 5)

# Test removing a product from the cart
# shopping_cart.removeProduct(product2)

# Test getting the contents of the cart
cart_contents = shopping_cart.getContents()

# Print the cart contents
for product in cart_contents:
    print(product)

shopping_cart.printCartContents()

# Export the cart contents to JSON
# cart_json = shopping_cart.to_json()
# print(cart_json)