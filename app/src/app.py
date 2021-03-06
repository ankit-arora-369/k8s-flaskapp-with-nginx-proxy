from flask import Flask, jsonify
app = Flask(__name__)
from flask import Flask, jsonify
app = Flask(__name__)

country_list = [
    'Nepal',
    'India',
    'Germany',
    'Netherlands'
]

@app.route('/')
def index():
    response_dict = {
        "message": "Welcome to FlaskApp"
    }
    return jsonify(response_dict)

@app.route('/names')
def countries():
    country_dict = {
        'countries': country_list,
        'total': len(country_list)
    }
    return jsonify(country_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8083)
