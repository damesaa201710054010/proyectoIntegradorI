from flask import Flask
from flask_cors import CORS
from datetime import date
from datetime import datetime
from flask import request, Response, jsonify

app = Flask(__name__)
CORS(app)

tipo_medicion = {'Sensor': 'TSL2561', 'Variable': 'Luz Solar', 'Unidades': 'lx'}

mediciones = [
    {'fecha': '2019-08-06 11:10:00', **tipo_medicion, 'Valor': 5000 },
    {'fecha': '2019-08-10 11:00:00', **tipo_medicion, 'Valor': 15000 },
    {'fecha': '2019-08-11 12:00:00', **tipo_medicion, 'Valor': 20000 },
    {'fecha': '2019-08-11 14:56:00', **tipo_medicion, 'Valor': 7500 },
    {'fecha': '2019-08-11 15:47:00', **tipo_medicion, 'Valor': 25000 },
    {'fecha': '2019-08-07 16:30:00', **tipo_medicion, 'Valor': 5000 },
    {'fecha': '2019-08-09 17:32:00', **tipo_medicion, 'Valor': 15000 },
    {'fecha': '2019-08-20 19:37:00', **tipo_medicion, 'Valor': 15000 },
    {'fecha': '2019-08-30 23:45:00', **tipo_medicion, 'Valor': 12000 },
    {'fecha': '2019-08-31 09:15:00', **tipo_medicion, 'Valor': 2000 },
    {'fecha': '2019-08-24 06:20:00', **tipo_medicion, 'Valor': 1000 },
    {'fecha': '2019-08-25 01:09:00', **tipo_medicion, 'Valor': 500 },
    {'fecha': '2019-08-27 15:38:00', **tipo_medicion, 'Valor': 6000 },
    {'fecha': '2019-08-29 16:49:00', **tipo_medicion, 'Valor': 10000 },
    {'fecha': '2019-08-22 13:59:00', **tipo_medicion, 'Valor': 10500 },
    {'fecha': '2019-08-21 14:07:00', **tipo_medicion, 'Valor': 5000 },
    {'fecha': '2019-08-05 19:20:00', **tipo_medicion, 'Valor': 3000 },
    {'fecha': '2019-08-01 21:23:00', **tipo_medicion, 'Valor': 5000 },
    {'fecha': '2019-08-10 22:33:00', **tipo_medicion, 'Valor': 1000 },
]

@app.route('/mediciones')
def getAll():
    return jsonify(mediciones)

@app.route('/mediciones/value', methods = ['POST'])
def POST(): 
    value = value.request.form.get('value')
    now = datetime.now()
    format = now.strftime('Año: %Y, Mes: %m, Día :%d, Hora: %H, Minutos: %M, Segundos: %S')
    return jsonify(mediciones.append({'fecha':format, **tipo_medicion, 'Valor': value}))

app.run(port=5000, debug=True)

    



