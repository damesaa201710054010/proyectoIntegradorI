from flask import Flask
from flask_cors import CORS
from datetime import date
from datetime import datetime
from flask import request, Response, jsonify, render_template
from api.controllers.participantes import *

app = Flask(__name__)
CORS(app)

tipo_medicion = {'Sensor': 'TSL2561', 'Variable': 'Luz Solar', 'Unidades': 'lx'}

mediciones = [ ]

@app.route('/listarMediciones')
def getAll():
    return (participantes.list())

@app.route('/mediciones/addValue', methods = ['POST'])
def POST():
    body = request.json 
    #Body = request.get_json(force=True)
    #fecha = Body['fecha']
    #value = Body['value']
    #format = fecha.strftime('Año: %Y, Mes: %m, Día :%d, Hora: %H, Minutos: %M, Segundos: %S')
    #mediciones.append({'fecha':fecha, **tipo_medicion, 'Valor': value})
    return (participantes.create(body))

@app.route('/mediciones/media', methods = ['GET'])
def getMedia():
    mediciones = participantes.list()
    sum  = 0
    j = 0
    for i in mediciones:
        medicion = i['Valor']  
        sum = sum + medicion
        j = j+1
    media = sum/j
    respuesta = {'Media' : media}
    return jsonify(respuesta)



