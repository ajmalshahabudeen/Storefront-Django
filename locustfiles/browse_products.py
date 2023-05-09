from random import randint
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    # Viewing products
    @task(2)
    def view_products(self):
        collection_id = randint(2, 6)
        self.client.get(
            f'/store/products/?collection_id={collection_id}',
            name='/store/products' #group name
        )
    
    # Viewing products details
    @task(4)
    def view_product(self):
        product_id = randint(1, 1000)
        self.client.get(
            f'/store/products/{product_id}',
            name='/store/product/:id'
        )
        
    # Add product to cart
    @task(1)
    def add_to_cart(self):
        product_id = randint(1, 10) # 1 to 10 is to check performance for duplicate/updating a cart
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name='/store/carts/items',
            json={'product_id': product_id, 'quantity': 1}
        )
        
    def on_start(self): # its not a task but a life-cycle hook
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result[id]