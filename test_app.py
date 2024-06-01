import unittest
import warnings
from app import app

class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_index_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data.decode(), "<p>Hello, World!</p>")

    def test_gethrm(self):
        response = self.app.get("/hrm")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Red Cross" in response.data.decode())

    def test_gethrm_by_id(self):
        response = self.app.get("/hrm/1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("3" in response.data.decode())


if __name__ == "__main__":
    unittest.main()