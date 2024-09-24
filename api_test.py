from flask import Flask





app = Flask(__name__)


@app.route('/getcode', methods=['GET'])
def getcode():
    # คุณสามารถส่งค่าตัวเลขหรือข้อความตามต้องการ
    return "12345"  # หรือจะเป็นข้อความอื่นๆ เช่น "Hello, this is your code"

@app.route('/plus/<int:num1>/<int:num2>')
def plus(num1, num2):
    result = num1 + num2
    return str(result)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
