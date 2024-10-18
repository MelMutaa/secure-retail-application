# order.py - Basic order management functionality

class OrderManager:
    def __init__(self):
        self.orders = []

    def place_order(self, user, basket):
        """Place a new order."""
        order = {
            'user': user,
            'basket': basket,
            'status': 'Pending'
        }
        self.orders.append(order)
        print(f"Order placed successfully for {user}!")

    def view_orders(self, user):
        """View orders for a specific user."""
        user_orders = [order for order in self.orders if order['user'] == user]
        if user_orders:
            for order in user_orders:
                print(f"Order for {order['user']} - Status: {order['status']}")
        else:
            print("No orders found.")
