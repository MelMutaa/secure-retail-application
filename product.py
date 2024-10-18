# product.py - Basic Product management functionality

import json


class ProductManager:
    def __init__(self):
        self.products_file = 'data/products.json'
        self.load_products()

    def load_products(self):
        """Load product data from JSON file."""
        with open(self.products_file, 'r') as file:
            self.products = json.load(file)

    def save_products(self):
        """Save product data to JSON file."""
        with open(self.products_file, 'w') as file:
            json.dump(self.products, file, indent=4)

    def view_products(self):
        """View all available products."""
        for product_id, product_info in self.products.items():
            print(f"ID: {product_id} - Name: {product_info['name']} - Price: ${product_info['price']}")

    def add_product(self):
        """Add a new product to the store."""
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))

        product = {
            'name': name,
            'price': price
        }

        self.products[product_id] = product
        self.save_products()
        print(f"Product {name} added successfully.")

    def update_product(self):
        """Update an existing product's information."""
        product_id = input("Enter the product ID to update: ")
        if product_id in self.products:
            new_name = input("Enter new product name: ")
            new_price = float(input("Enter new product price: "))
            self.products[product_id] = {'name': new_name, 'price': new_price}
            self.save_products()
            print(f"Product {product_id} updated successfully.")
        else:
            print(f"Product {product_id} not found.")

    def delete_product(self):
        """Delete an existing product from the store."""
        product_id = input("Enter the product ID to delete: ")
        if product_id in self.products:
            del self.products[product_id]
            self.save_products()
            print(f"Product {product_id} deleted successfully.")
        else:
            print(f"Product {product_id} not found.")

    def add_to_basket(self):
        """Dummy function to add product to user's basket."""
        print("Product added to basket.")

    def remove_from_basket(self):
        """Dummy function to remove product from user's basket."""
        print("Product removed from basket.")
