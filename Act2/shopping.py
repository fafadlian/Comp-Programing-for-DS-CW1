import json
import uuid

class Product:
    def __init__(self, name, price, quantity, brand):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.brand = brand
        self.identifier = str(uuid.uuid4().int)[:13]

    def to_dct(self):
        product_dict = {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'identifier': self.identifier,
            'brand': self.brand
        }
        return product_dict
    
    def to_json(self):
        product_dict = self.to_dct()
        product_json = json.dumps(product_dict, indent=4)
        return product_json
    
class Clothing(Product):
    def __init__(self, name, price, quantity, brand, size, material):
        super().__init__(name, price, quantity, brand)
        self.size = size
        self.material = material

    def to_json(self):
        product_dict = super().to_dct()
        product_dict.update({'size': self.size, 'material': self.material})
        product_json = json.dumps(product_dict, indent=4)
        return product_json

class Food(Product):
    def __init__(self, name, price, quantity, brand, expiry_date, gluten_free, suitable_for_vegan):
        super().__init__(name, price, quantity, brand)
        self.expiry_date = expiry_date
        self.gluten_free = gluten_free
        self.suitable_for_vegan = suitable_for_vegan

    def to_json(self):
        product_dict = super().to_dct()
        product_dict.update({'expiry_date': self.expiry_date, 'gluten_free': self.gluten_free, 'suitable_for_vegan': self.suitable_for_vegan})
        product_json = json.dumps(product_dict, indent=4)
        return product_json
    
class ShoppingCart:
    def __init__(self):
        self.cart = []
    
    def addProduct(self, product):
        self.cart.append(product)
    
    def removeProduct(self, product):
        if product in self.cart:
            self.cart.remove(product)

    def getContents(self):
        sort_crt = sorted(self.cart, key=lambda product: product.name)
        return sort_crt
    
    def changeProductQuantity(self, product, quantity):
        if product in self.cart:
            product.quantity = quantity

    def printCartContents(self):
        if not self.cart:
            print("The cart is empty.")
        else:
            print("Cart Contents:")

            for product in self.cart:
                print(f"{product.name} - Quantity: {product.quantity}")

    def to_json(self):
        cart_contents = [product.to_json() for product in self.cart]
        return json.dumps(cart_contents, indent=4)