from flask import Flask,jsonify,request 
from datetime import datetime
from Crud import CRUD 
from dotenv import load_dotenv 
import os






app = Flask(__name__)

#Conectando ao banco de dados
load_dotenv()
password = os.getenv("PASSWORD")
user = os.getenv("USER")
host = os.getenv("HOST")
database = os.getenv("DATABASE")
crud = CRUD(user=user,password=password,host=host,database=database)



@app.errorhandler(404)
def page_not_found(erro):
    return erro

@app.errorhandler(500)
def internal_server_error(erro):
    return "Internal Server Error",erro


#Gets

@app.route("/MensurementUnits",methods=["GET"])
def GetMensurementUnits():
    """ retorna todas as unidades de medida do banco com id simbulo e descrição"""
    resultado = crud.read_mensurement_units()
    if resultado != False:
        return jsonify(resultado),200
    else:
        erro = {'message': 'No mensurement Units', 'status': 404}
        return jsonify(erro),erro["status"]

@app.route("/UserDevices/<string:user>",methods=["GET"])
def get_all_user_devices(user):
    """ retorna todos os sensores de um usuario"""
    retorno = crud.read_user_devices(user=user)

    if retorno == False:
        erro = {'message': 'User Not found', 'status': 404}
        return jsonify(erro), erro["status"]
    
    elif retorno[0] == {}:
        erro = {'message': 'No User Info', 'status': 404}
        return jsonify(erro), erro["status"]
    else:
        return jsonify(retorno)

@app.route("/UserDevice/<string:SensorKey>",methods=["GET"])
def get_user_device(SensorKey):
    """ retorna um sensor expecifico de um usuario necessário a key do dispositivo"""
    retorno = crud.read_user_device(sensorkey=SensorKey)

    if retorno[0] == {}:
        erro = {'message': 'This Sensor Device Do not Exist', 'status': 404}
        return jsonify(erro), erro["status"]
    
    else:
        return jsonify(retorno)

@app.route("/UserDevice/Stream/<string:StreamKey>",methods=["GET"])
def get_device_stream(StreamKey):
    """ retorna uma stream de um sensor epecifico de um usuario necessário uma 'stream key' para poder acessar a 
    stream especifica"""
    retorno = crud.read_device_stream(streamkey=StreamKey)
    if len(retorno) == 0:
        erro = {'message': 'This Stream Do not Exist', 'status': 404}
        return jsonify(erro), erro["status"]
    else:
        return jsonify(retorno)

#Posts                       #                                          #

@app.route("/NewDevice/<string:user>",methods=["POST"])
def create_new_device(user):
    """ Recebe um label e uma description via json  e retorna um json com as informações do Sensor device ja registrado"""
    data = request.get_json()
    if "label" in data[0] and "description" in data[0]:
        label = data[0]["label"]
        description = data[0]["description"]
        return jsonify(crud.create_new_device(user=user,label=label,description=description)),201
    
    else:
        erro = {'message': 'Invalid JSON', 'status': 400}
        return jsonify(erro), erro["status"]

@app.route("/NewStream/SensorKey/<string:SensorKey>",methods=["POST"])
def create_new_stream (SensorKey):
    """ recebe um json com lebel e unitId registra no banco e retorna o registro com id,key,unitID,deviceId,mensurementCount,
    necessário ter o nome do usuario e a key do dispositivo o retorno vai em json"""
    
    data = request.get_json()
    if "label" in data[0] and "unitId" in data[0]:
        label = data[0]["label"]
        unitId = data[0]["unitId"]
        return jsonify(crud.create_new_stream(sensorKey=SensorKey,label=label,unitId=unitId)),201
    
    else:
        erro = {'message': 'Invalid JSON', 'status': 400}
        return jsonify(erro), erro["status"]

@app.route("/NewStreamData/StreamKey/<string:StreamKey>",methods=["POST"])
def create_new_stream_data(StreamKey):
    """ recebe um timestemp e um valor registra e retorna id,timestamp, valor e unitId ,
    necessário ter o nome do usuario , a key do dispositivo e a key da stream o retorno vai em json"""

    data = request.get_json()
    if "timestamp" in data[0] and "value" in data[0]:
        timestamp_recebido = data[0]["timestamp"]
        value = data[0]["value"]
        timestamp_atual = datetime.fromtimestamp(timestamp_recebido)
        mysql_date = timestamp_atual.strftime('%Y-%m-%d %H:%M:%S')
        return  jsonify(crud.create_new_stream_data(streamKey=StreamKey,timeStamp=mysql_date,value=value)),201
    
    else:
        erro = {'message': 'Invalid JSON', 'status': 400}
        return jsonify(erro), erro["status"]


    

if __name__ == "__main__":
    app.run(port=5000,host="localhost",debug=True)