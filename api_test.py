from flask import Flask
import unittest 

app = Flask(__name__)


@app.route('/getcode', methods=['GET'])
def getcode():
    # คุณสามารถส่งค่าตัวเลขหรือข้อความตามต้องการ
    return "12345"  # หรือจะเป็นข้อความอื่นๆ เช่น "Hello, this is your code"

@app.route('/plus/<int:num1>/<int:num2>')
def plus(num1, num2):
    result = num1 + num2
    return str(result)

class TestAddition(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_plus(self):
    # ทดสอบการเรียก /plus/1/2
        result = self.app.get('/plus/1/2')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), str(3))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
