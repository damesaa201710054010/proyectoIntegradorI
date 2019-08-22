from flask import Flask
from flask import request, Response, jsonify

app = Flask(__name__)
CORS(app)

tipo_medicion = {'Sensor': 'TSL2561', 'Variable': 'Luz Solar', 'Unidades': 'lx'}

mediciones = [
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }
    {'fecha': '2019-08-07 12:24:00', **tipo_medicion, 'Valor': 5000 }

]

@app.route('/')


