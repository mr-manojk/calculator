from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    op = data.get('op')
    try:
        if op == 'add':
            result = a + b
        elif op == 'sub':
            result = a - b
        elif op == 'mul':
            result = a * b
        elif op == 'div':
            result = a / b
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)