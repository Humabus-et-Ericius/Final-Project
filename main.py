from flask import Flask, render_template, request

app = Flask(__name__)
counter = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global counter
    if request.method == 'POST':
        # Проверяем, какая кнопка была нажата
        if 'increase' in request.form:
            counter += 1
        elif 'decrease' in request.form:
            counter -= 1
    return render_template('index.html', counter=counter)



app.run(debug=True)