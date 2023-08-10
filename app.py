from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import text
app=Flask(__name__)
#app.config['SQL_ALCHEMY_DATABASE_URI']='sqlite:///database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://uwcz1z8tw0nrh0ey:OeX1Pjhhuve1VA5v0Pd8@bmotoxcjvbuzkz2ic55p-mysql.services.clever-cloud.com:3306/bmotoxcjvbuzkz2ic55p'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

@app.route('/',methods=['GET'])
def home():
    print("API CONECTADA")

    # Retornar los resultados como JSON en la respuesta
    return jsonify("Api Conectada")

@app.route('/actual',methods=['GET'])
def actual():
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta SELECT *
    query = text("SELECT * FROM actual ORDER BY id DESC LIMIT 1")
    result = conn.execute(query)
    column_names = result.keys()

    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    print(results_list)
    # Cerrar la conexión
    conn.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify(results_list)

@app.route('/morning',methods=['GET'])
def morning():
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta SELECT *
    query = text("SELECT * FROM mañana")
    result = conn.execute(query)
    column_names = result.keys()

    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    # Cerrar la conexión
    conn.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify(results_list)

@app.route('/afternoon',methods=['GET'])
def afternoon():
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta SELECT *
    query = text("SELECT * FROM tarde")
    result = conn.execute(query)
    column_names = result.keys()

    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    # Cerrar la conexión
    conn.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify(results_list)

@app.route('/night',methods=['GET'])
def night():
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta SELECT *
    query = text("SELECT * FROM noche")
    result = conn.execute(query)
    column_names = result.keys()

    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    # Cerrar la conexión
    conn.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify(results_list)
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")
    
