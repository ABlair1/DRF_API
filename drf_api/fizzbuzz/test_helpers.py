from datetime import datetime
from fizzbuzz.models import FizzBuzz

MOCK_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " \
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"


class FizzBuzzTestBuilder():
    """
    Builds objects with data that can be used for testing FizzBuzz API
    endpoints.
    """
    def __init__(self):
        self.data = {}
        pass

    def get_data(self):
        return self.data

    def add_fizzbuzz_id(self):
        self.data["fizzbuzz_id"] = str(FizzBuzz.objects.count() + 1)

    def add_useragent(self):
        self.data["useragent"] = MOCK_USER_AGENT

    def add_message(self):
        self.data["message"] = "Hello, World!"

    def add_creation_date(self):
        self.data["creation_date"] = datetime.now().isoformat() + "Z"

    def add_invalid_field(self):
        self.data["info"] = "Hello, World!"
