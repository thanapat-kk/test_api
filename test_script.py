import unittest
from api_test import app

class TestAddition(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_plus(self):
    # ทดสอบการเรียก /plus/1/2
        result = self.app.get('/plus/1/2')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), str(3))