from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result_value = num1 + num2
        elif operation == 'subtract':
            result_value = num1 - num2
        elif operation == 'multiply':
            result_value = num1 * num2
        else: 
            if num2 == 0:
                result_value = "Error: Division by zero" 
            else:
                num1 / num2
        
    except:
        result_value = "Please enter valid numbers."

    return render_template('result.html', result=result_value)

if __name__ == '__main__':
    app.run(debug=True)
