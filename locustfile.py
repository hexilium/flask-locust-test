from locust import HttpUser, between, task


class Index(HttpUser):
    weight = 5
    @task
    def index(self):
        self.client.get("/index")
    wait_time = between(1, 5)


class MoreLoad(HttpUser):
    weight = 1
    @task
    def moreload(self):
        self.client.get("/moreload")
    wait_time = between(1, 5)
