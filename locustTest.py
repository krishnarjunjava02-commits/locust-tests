from locust import HttpUser, task, between

class TricentisUser(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def load_home(self):
        self.client.get("/")

    @task(1)
    def load_about(self):
        self.client.get("/about")

    @task(3)
    def search_product(self):
        self.client.get("/search?q=testing")

    @task(1)
    def add_to_cart(self):
        self.client.post("/cart", {"product_id": "1234", "quantity": 1})

    @task(1)
    def checkout(self):
        self.client.get("/checkout")
