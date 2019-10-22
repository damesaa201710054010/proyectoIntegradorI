
from api.baseDeDatos.baseDeDatos import cnx
from flask import jsonify, request

class participantes:
    global cur
    cur = cnx.cursor()
    def list():
        lista = []
        cur.execute("SELECT * FROM participantes")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        cnx.close()
        return jsonify(lista)
    
    def create(body):
        data = (body['cedula'], body['nombre'], body['actividad'], 
                body['estrato'], body['foto'])
        sql = "INSERT INTO evergreen.participantes(cedula, nombre, actividad, estrato, foto) VALUES(%s,%s,%s,%s,%s)"
        cur.execute(sql, data)
        cnx.commit()
        return {'estado':"Insertado"}, 200