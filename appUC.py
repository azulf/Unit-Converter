from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Ambil input dari form
    value = request.form.get('value')
    unit = request.form.get('unit')
    
    # Lakukan konversi sederhana (contoh: meter ke kilometer)
    if unit == 'meter':
        result = float(value) / 1000
        converted_unit = 'kilometer'
    else:
        result = 'Invalid unit'
        converted_unit = ''
    
    # Kirim hasil ke template
    return render_template('index.html', result=result, converted_unit=converted_unit)

@app.route('/Length', methods=['POST'])
def length():
    # Ambil input dari form
    value = request.form.get('value')
    unit = request.form.get('unit')
    
    # Lakukan konversi panjang sederhana (contoh: meter ke kilometer)
    if unit == 'meter':
        result = float(value) / 1000
        converted_unit = 'kilometer'
    else:
        result = 'Invalid unit'
        converted_unit = ''
    
    # Kirim hasil ke template
    return render_template('index.html', result=result, converted_unit=converted_unit)

@app.route('/Weight', methods=['POST'])
def weight():   
    # Ambil input dari form
    value = request.form.get('value')
    unit = request.form.get('unit')
    
    # Lakukan konversi berat sederhana (contoh: gram ke kilogram)
    if unit == 'gram':
        result = float(value) / 1000
        converted_unit = 'kilogram'
    else:
        result = 'Invalid unit'
        converted_unit = ''
    
    # Kirim hasil ke template
    return render_template('index.html', result=result, converted_unit=converted_unit)

@app.route('/Temperature', methods=['POST'])
def temperature():
    # Ambil input dari form
    value = request.form.get('value')
    unit = request.form.get('unit')
    
    # Lakukan konversi suhu sederhana (contoh: Celsius ke Fahrenheit)
    if unit == 'Celsius':
        result = (float(value) * 9/5) + 32
        converted_unit = 'Fahrenheit'
    else:
        result = 'Invalid unit'
        converted_unit = ''
    
    # Kirim hasil ke template
    return render_template('index.html', result=result, converted_unit=converted_unit)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
