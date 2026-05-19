from flask import Flask, render_template, request

app = Flask(__name__)
counter = 0
counter0 = 0
counter1 = 0
counter2 = 0

def result_calculate():
    bottle_p_colef = 450
    bag_p_colef = 256
    box_p_colef = 551
    plate_p_colef = 200
    return bottle_p_colef * counter + bag_p_colef * counter0 + box_p_colef * counter1 + plate_p_colef * counter2


@app.route('/', methods=['GET', 'POST'])
def index():
    global counter, counter0, counter1, counter2
    if request.method == 'POST':
        # Проверяем, какая кнопка была нажата
        if 'increase' in request.form:
            counter += 1
        elif 'decrease' in request.form:
            if counter > 0:
                counter -= 1

        if 'increase0' in request.form:
            counter0 += 1
        elif 'decrease0' in request.form:
            if counter0 > 0:
                counter0 -= 1

        if 'increase1' in request.form:
            counter1 += 1
        elif 'decrease1' in request.form:
            if counter1 > 0:
                counter1 -= 1

        if 'increase2' in request.form:
            counter2 += 1
        elif 'decrease2' in request.form:
            if counter2 > 0:
                counter2 -= 1
        
        if 'reset' in request.form:
            counter = 0
            counter0 = 0
            counter1 = 0
            counter2 = 0
            
    return render_template('index.html', counter=counter, counter0=counter0, counter1=counter1, counter2=counter2)

@app.route('/result', methods=['POST'])
def submit_form():
    t1 = result_calculate()
    return render_template('result.html',
                           t1=t1)  

app.run(debug=True)
