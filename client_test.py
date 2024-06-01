import unittest
from client3 import fetch_data, process_data

class TestClient3(unittest.TestCase):

    def test_fetch_data(self):
        data = fetch_data()
        self.assertIsNotNone(data)

    def test_process_data(self):
        data = {"priceA": 100, "priceB": 200}
        processed = process_data(data)
        self.assertEqual(processed, {"priceA": 100, "priceB": 200})

if __name__ == "__main__":
    unittest.main()
