import json
from fizzbuzz.serializers import MSG_ERROR, HEADER_ERROR
from fizzbuzz.test_helpers import FizzBuzzTestBuilder, MOCK_USER_AGENT
from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class FizzBuzzTestCase(APITestCase):
    """
    Test suite for FizzBuzz API endpoints
    """
    def setUp(self):
        self.client = APIClient()
        self.url = "/fizzbuzz/"
        self.test_fb = FizzBuzzTestBuilder()

    def test_create_fizzbuzz(self):
        # Create valid POST request data and set User-Agent header
        self.test_fb.add_message()
        req_data = self.test_fb.get_data()
        self.client.credentials(HTTP_USER_AGENT=MOCK_USER_AGENT)

        response = self.client.post(
            self.url,
            req_data,
            format="json",
        )
        fizzbuzz = json.loads(response.content)

        self.assertEqual(response.status_code, 201)
        self.assertTrue("fizzbuzz_id" in fizzbuzz)
        self.assertTrue("useragent" in fizzbuzz)
        self.assertTrue("creation_date" in fizzbuzz)
        self.assertTrue("message" in fizzbuzz)
        self.assertEqual(fizzbuzz["message"], req_data["message"])        

    def test_create_multiple_fizzbuzz(self):
        # Create valid POST request data
        self.test_fb.add_message()
        req_data = self.test_fb.get_data()

        # Set User-Agent header for POST request
        self.client.credentials(HTTP_USER_AGENT=MOCK_USER_AGENT)
        response_1 = self.client.post(
            self.url,
            req_data,
            format="json",
        )
        response_2 = self.client.post(
            self.url,
            req_data,
            format="json",
        )
        response_3 = self.client.post(
            self.url,
            req_data,
            format="json",
        )
        fizzbuzz_1 = json.loads(response_1.content)
        fizzbuzz_2 = json.loads(response_2.content)
        fizzbuzz_3 = json.loads(response_3.content)

        # Verify multiple objects created and id increments with each
        self.assertEqual(response_1.status_code, 201)
        self.assertEqual(response_2.status_code, 201)
        self.assertEqual(response_3.status_code, 201)
        self.assertEqual(
            int(fizzbuzz_1["fizzbuzz_id"]) + 1,
            int(fizzbuzz_2["fizzbuzz_id"])
        )
        self.assertEqual(
            int(fizzbuzz_2["fizzbuzz_id"]) + 1,
            int(fizzbuzz_3["fizzbuzz_id"])
        )

    def test_create_invalid_header(self):
        # Create valid POST request data
        self.test_fb.add_message()
        req_data = self.test_fb.get_data()

        # Send POST request without setting User-Agent header
        response = self.client.post(
            self.url,
            req_data,
            format="json",
        )
        response_content = json.loads(response.content)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_content, HEADER_ERROR)

    def test_create_invalid_fizzbuzz_1(self):
        # Create invalid request data that has all fields
        self.test_fb.add_message()
        self.test_fb.add_fizzbuzz_id()
        self.test_fb.add_useragent()
        self.test_fb.add_creation_date()
        req_data = self.test_fb.get_data()

        # Set User-Agent header for POST request
        self.client.credentials(HTTP_USER_AGENT=MOCK_USER_AGENT)
        response = self.client.post(
            self.url,
            req_data,
            format="json",
        )
        response_content = json.loads(response.content)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_content, MSG_ERROR)

    def test_create_invalid_fizzbuzz_2(self):
        # Create invalid request data with no message and extra field
        self.test_fb.add_invalid_field()
        req_data = self.test_fb.get_data()

        # Set User-Agent header for POST request
        self.client.credentials(HTTP_USER_AGENT=MOCK_USER_AGENT)
        response = self.client.post(
            self.url,
            req_data,
            format="json",
        )
        response_content = json.loads(response.content)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_content, MSG_ERROR)

    def test_get_fizzbuzz_list(self):
        # Create valid POST request data and header
        self.test_fb.add_message()
        req_data = self.test_fb.get_data()
        self.client.credentials(HTTP_USER_AGENT=MOCK_USER_AGENT)

        n = 4
        for i in range(n):
            self.client.post(self.url, req_data, format="json")
        response = self.client.get(self.url)
        fizzbuzz_list = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(fizzbuzz_list), n)
        for i in range(n):
            self.assertTrue("fizzbuzz_id" in fizzbuzz_list[i])
            self.assertTrue("useragent" in fizzbuzz_list[i])
            self.assertTrue("creation_date" in fizzbuzz_list[i])
            self.assertTrue("message" in fizzbuzz_list[i])

    def test_get_fizzbuzz_single(self):
        # Create valid POST request data and header
        self.test_fb.add_message()
        req_data = self.test_fb.get_data()
        self.client.credentials(HTTP_USER_AGENT=MOCK_USER_AGENT)

        post_response = self.client.post(
            self.url,
            req_data,
            format="json",
        )
        fb_id = json.loads(post_response.content)["fizzbuzz_id"]
        print("fb_id", fb_id)

        # Get fizzbuzz with id
        get_response = self.client.get(self.url + fb_id + "/")
        fizzbuzz = json.loads(get_response.content)

        self.assertEqual(get_response.status_code, 200)
        self.assertTrue("fizzbuzz_id" in fizzbuzz)
        self.assertTrue("useragent" in fizzbuzz)
        self.assertTrue("creation_date" in fizzbuzz)
        self.assertTrue("message" in fizzbuzz)
        self.assertEqual(fizzbuzz["message"], req_data["message"])        
