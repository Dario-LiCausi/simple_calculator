from flask import Flask, request, render_template, jsonify
from simpleeval import simple_eval

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json() # get the operation from frontend
    expression = data.get('expression', '')

    try:
        result = simple_eval(expression) # takes care of the operation entered by the user without any limitation of variables
    except ZeroDivisionError:
        result = 'Error: No / by 0'
    except Exception:
        result = 'Error'

    return jsonify({'result': result}) # send the resoult back to frontend

if __name__ == '__main__':
    app.run(debug=True)