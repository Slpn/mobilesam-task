import unittest
import requests
from PIL import Image
import io

url = "http://localhost:80/segment-image"
invalid_image_path = "resources/invalid_image.txt"
class TestFastAPI(unittest.TestCase):

    def test_invalid_image(self):
        with open(invalid_image_path, "rb") as file:
            response = requests.post(url, files={"file": file})

        self.assertEqual(response.status_code, 400)
        result = response.json()
        self.assertIn("error", result)

    def test_no_file(self):
        response = requests.post(url, files={})

        self.assertEqual(response.status_code, 422)
        result = response.json()
        self.assertIn("detail", result)

    def test_non_image_file(self):
        response = requests.post(url, files={"file": io.BytesIO(b"this is not an image")})

        self.assertEqual(response.status_code, 400)
        result = response.json()
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
