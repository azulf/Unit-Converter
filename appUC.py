from flask import Flask, render_template, request
from Converter import Converter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Length', methods=['GET','POST'])
def length():
    if request.method == 'GET':
        return render_template('index.html', active_form='Length')
    elif request.method == 'POST':
        value = request.form.get('value')
        unit = request.form.get('unit_from')
        unit_to = request.form.get('unit_to')
        
        result = Converter.convert_length(value, unit, unit_to)
        converted_unit = unit_to
    
        # Kirim hasil ke template
        return render_template('index.html', result=result, converted_unit=converted_unit, active_form='Length')


@app.route('/Weight', methods=['GET','POST'])
def weight():   
    if request.method == 'GET':
        return render_template('index.html', active_form='Weight')
    elif request.method == 'POST':
        value = request.form.get('value')
        unit = request.form.get('unit_from')
        unit_to = request.form.get('unit_to')
        
        result = Converter.convert_weight(value, unit, unit_to)
        converted_unit = unit_to
        
        # Kirim hasil ke template
        return render_template('index.html', result=result, converted_unit=converted_unit, active_form='Weight')

@app.route('/Temperature', methods=['GET','POST'])
def temperature():
    if request.method == 'GET':
        return render_template('index.html', active_form='Temperature')
    elif request.method == 'POST':
        value = request.form.get('value')
        unit = request.form.get('unit_from')
        unit_to = request.form.get('unit_to')
        
        result = Converter.convert_temperature(value, unit, unit_to)
        converted_unit = unit_to
        
        # Kirim hasil ke template
        return render_template('index.html', result=result, converted_unit=converted_unit, active_form='Temperature')



if __name__ == '__main__':
    app.run(port=8080, debug=True)
