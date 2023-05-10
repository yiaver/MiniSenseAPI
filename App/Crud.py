<<<<<<< HEAD
import mysql.connector
from datetime import datetime
import logging
import uuid 

logging.basicConfig(level=logging.ERROR, format='%(levelname)s %(asctime)s - %(message)s')
#voltar aqui e tratar possiveis erros

class ErrosPersonalizados(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

class CRUD():
    def __init__(self,user:str,password:str,host:str,database:str) -> None:
        self.user = user
        self.password =password
        self.host = host
        self.database = database
        #tratando erros de conexão e informarções erradas com o servidor
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            test_database = f"USE {database};"
            cursor.execute(test_database)

            if None in (user,database,password,host):
                raise ErrosPersonalizados("None type Error")
            
            print(f"++++ Conectado com sucesso a {database} como {user} no host {host} ++++")
            connection.close()
        
        except Exception as err:
            print(f"XXXX user, database, host == {[user,database,host]} XXXX")
            logging.error(f"XXXXX Connection error : {err} XXXXXX")

        #criando key aleatoria com letras e numeros 

    @property    
    def randkey(self):
        return self.__randomKey

    
    
    def shall_not_pass(self,obj):
        """ None and False  shall not pass!!"""
        if obj == False or obj == None:
            return False
        else:
            return True
    
    def findComplex(self,column,table,column1,obj1,column2,obj2):
        """Retorna o ultimo resultado de uma pesquisa no banco usando essa query:
        SELECT {column} FROM {table} WHERE {column1} = '{obj1}' AND {column2} = '{obj2}';"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            query_finder = f"SELECT {column} FROM {table} WHERE {column1} = '{obj1}' AND {column2} = '{obj2}';"
            cursor.execute(query_finder)
            result = cursor.fetchall()
            if self.shall_not_pass(result) and len(result) > 0:
                finder_result = result[-1][0]
                connection.close()
                return finder_result
            else:
                connection.close()
                return False
        except Exception as err:
            logging.error(f"Error in {self.findComplex.__name__} : {err}")

    def findFirstOne(self,column,table,column1,obj):
        """Procura um iten especifico em uma tabela com essa query:\n
            SELECT {column} FROM {table} WHERE {column2} = '{obj}';"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            query_finder = f"SELECT {column} FROM {table} WHERE {column1} = '{obj}';"
            cursor.execute(query_finder)
            result = cursor.fetchone()
            if self.shall_not_pass(result) and len(result) > 0:
                finder_result = result[0]
                connection.close()
                return finder_result
            else:
                connection.close()
                return False
        except Exception as err:
            logging.error(f"Error in {self.findFirstOne.__name__} : {err}")
        
    
    def findAllInARow(self,table,column2,obj):
        """Procura uma row especifica em uma tabela com essa query:\n
            SELECT * FROM {table} WHERE {column2} = '{obj}';"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            query_finder = f"SELECT * FROM {table} WHERE {column2} = '{obj}';"
            cursor.execute(query_finder)
            result = cursor.fetchall()
            if self.shall_not_pass(result) and len(result) > 0:
                connection.close()
                return result
            else:
                connection.close()
                return False
        except Exception as err:
            logging.error(f"Error in {self.findAllInARow.__name__} : {err}")
        
    
    def insert(self,tabela:str,columnList:str,valueList:list):
        """Insere itens em uma tabela com essa query:\n
           INSERT INTO {tabela} {columnList} VALUES {lista_de_valores};"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            retira_colchetes = lambda x: str(x).replace("[","(").replace("]",")")
            lista_de_valores = retira_colchetes(valueList)
            insert_device_information =f"INSERT INTO {tabela} {columnList} VALUES {lista_de_valores};"
            cursor.execute(insert_device_information)
            connection.commit()
            connection.close()
            return True
        except Exception as err:
            logging.error(f"Error in {self.insert.__name__} : {err}")
       
    
    def update(self,table:str,column1:str,value1,whereColumn:str,whereValue):
        """Atualiza um valor em uma row com essa query:\n
           UPDATE {table} SET {column1} = {value1} WHERE {whereColumn} = {whereValue};"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            updateQuery = f"UPDATE {table} SET {column1} = {value1} WHERE {whereColumn} = {whereValue}"
            cursor.execute(updateQuery)
            connection.commit()
            connection.close()
            return True
        
        except Exception as err:
            logging.error(f"Error in {self.update.__name__} : {err}")
    
    
    def create_new_device(self,user:str,label:str,description:str):
        try:
            #gerando key aleatoria
            randkey_new_device = f"{uuid.uuid4()}".replace("-","")
            #find user id
            userid = self.findFirstOne("userId","user","name",user)
            if userid != False:
                #inserindo dados na tabela
                self.insert("sensordevice","(Akey,label,user_userId,description)",[f'{randkey_new_device}',f'{label}',userid,f'{description}'])
                #pegando id do device
                device_id = self.findFirstOne("SensorDeviceID ","sensordevice","Akey",randkey_new_device)
                #retorno Pra api
                device_api_return = [{"id":device_id,"key":randkey_new_device,"label":label,"description":description}]
                return device_api_return
            else:
                return False
        except Exception as err:
            logging.error(f"Error in {self.create_new_device.__name__} : {err}")

   
    def create_new_stream(self,sensorKey:str,label:str,unitId:int):
        try:
            #registro no banco de dados
            randkey_new_device = f"{uuid.uuid4()}".replace("-","")
            sensorid = self.findFirstOne("SensorDeviceID","sensordevice","Akey",sensorKey)
            if self.shall_not_pass(sensorid):
                valueList = [sensorid,randkey_new_device,label,unitId,0,0]
                self.insert("devicestream","(SensorDeviceID,Akey,label,MensurementUnitID,anabled,mensurementCount)",valueList=valueList)
                streamid = self.findFirstOne("DataStreamID","devicestream","Akey",randkey_new_device)
                mensurementcount = self.findFirstOne("mensurementCount","devicestream","Akey",randkey_new_device)
                #retorno Pra api
                strem_api_return = [{"id":streamid,"key":randkey_new_device,"label":label,"unitId":unitId,"deviceId":sensorid,"meansurementCount":mensurementcount}]
                return strem_api_return
            else:
                return False
            
        except Exception as err:
            logging.error(f"Error in {self.create_new_stream.__name__} : {err}")

        
    
    def create_new_stream_data(self,streamKey:str,timeStamp:int,value:float):
        try:
            #registro no banco de dados
            mensurementUnitId = self.findFirstOne("MensurementUnitID","devicestream","Akey",streamKey)
            streamId = self.findFirstOne("DataStreamID","devicestream","Akey",streamKey)
            mensurementcount = self.findFirstOne("mensurementCount","devicestream","Akey",streamKey)
            anabled = self.findFirstOne("anabled","devicestream","Akey",streamKey)
            if not False in (mensurementUnitId,streamId):
                valuelist = [streamId,timeStamp,mensurementUnitId,value]
                self.insert("streamdata","(DataStreamID,TimeStamp,MensurementUnitID,value)",valueList=valuelist)
                stream_data_id = self.findComplex("ID","streamdata","TimeStamp",timeStamp,"DataStreamID",streamId)
                #dar update no mensurament count and anabled
                plus_mensurement_count = mensurementcount+1
                #verifica e habilita o dispositivo
                if anabled == 0:
                    trueAnabled = 1
                    self.update("devicestream","anabled",trueAnabled,"DataStreamID",streamId)
                #retorno Pra api
                new_time_stamp = int(datetime.now().timestamp())
                stream_data_api_return = [{"id":stream_data_id,"timeStamp":new_time_stamp,"value":value,"unitId":mensurementUnitId}]
                self.update("devicestream","mensurementCount",plus_mensurement_count,"DataStreamID",streamId)
                return stream_data_api_return
            else:
                return False
        except Exception as err:
            logging.error(f"Error in {self.create_new_stream_data.__name__} : {err}")
        
    
    def read_mensurement_units(self):
        try:
            #criar logica de coleta de informações do banco de dados
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            cursor.execute("select * from mensurementunit;")
            get_all = cursor.fetchall()
            if get_all != None and len(get_all) > 0:
                mensurament_units_api_return = [{}]
                for index,iten in enumerate(get_all):
                    mensurament_units_api_return.append({})
                    for i,unit in enumerate(iten):
                        if i == 0:
                            mensurament_units_api_return[index]["id"] = unit
                        elif i == 1:
                            mensurament_units_api_return[index]["symbol"] = unit
                        elif i == 2:
                            mensurament_units_api_return[index]["description"] = unit
                        else:
                            continue
                    
                mensurament_units_api_return.pop(-1)
                return mensurament_units_api_return
            else:
                return False
            
        except Exception as err:
            logging.error(f"Error in {self.read_mensurement_units.__name__} : {err}")
        
    
    def read_user_devices(self,user):
        try:
            #criar logica de coleta de informações do banco de dados
            user_devices_api_return = [{}]
            userid = self.findFirstOne("userId","user","name",user)
            devices = self.findAllInARow("sensordevice","user_userID",userid)
            if self.shall_not_pass(userid) :

                if self.shall_not_pass(devices):
                    #percorre device 
                    for index,device in enumerate(devices):
                        #pega todas as streams de um device 
                        streams = self.findAllInARow("devicestream","SensorDeviceID",device[0])
                        #cataloga cada device
                        for idx, obj in enumerate(device):
                            if idx == 0:
                                user_devices_api_return[index]["id"]= obj
                            elif idx == 1:
                                user_devices_api_return[index]["key"]= obj
                            elif idx == 2:
                                user_devices_api_return[index]["label"]= obj
                            elif idx == 4:
                                user_devices_api_return[index]["description"]= obj
                                user_devices_api_return[index]["streams"] = []
                                user_devices_api_return.append({})
                            else:
                                continue
                        #cataloga cada stream de um device e adiciona nas streams do device 
                        if streams != False:
                            for stream in streams:
                                api_stream_return = {}
                                for i , component in enumerate(list(stream)):
                                    if i == 0:
                                        api_stream_return["id"] = component
                                    elif i == 1:
                                        api_stream_return["deviceId"] = component
                                    elif i == 2:
                                        api_stream_return["key"] = component
                                    elif i == 3:
                                        api_stream_return["label"]= component
                                    elif i == 4:
                                        api_stream_return["unitId"] = component
                                    elif i == 6:
                                        api_stream_return["measurementCount"] = component
                                        user_devices_api_return[index]["streams"].append(api_stream_return)
                                    else:
                                        continue
                    

                    user_devices_api_return.pop(-1)
                    return user_devices_api_return
                else:
                    return user_devices_api_return
            else:
                return False
        except Exception as err:
            logging.error(f"Error in {self.read_user_devices.__name__} : {err}")

    
    def read_user_device(self,sensorkey):
        try:
            devices = self.findAllInARow("sensordevice","Akey",sensorkey)
            deviceid=0
            streamid = 0
            user_device_api_return = [{}]
            if self.shall_not_pass(devices):
                #adicionando as informações do device ao json
                for index,device in enumerate(devices[0]):
                    if index == 0:
                        user_device_api_return[0]["id"]=  device
                        deviceid = device
                    if index == 1:
                        user_device_api_return[0]["key"]=  device
                        
                    if index == 2:
                        user_device_api_return[0]["label"]= device
                        
                    if index == 4:
                        user_device_api_return[0]["description"]= device
                        user_device_api_return[0]["streams"] = []
                        
                    else:
                        continue
                #adicionando as informações das streams ao json (streams)
                streams = self.findAllInARow("devicestream","SensorDeviceID",deviceid)
                if self.shall_not_pass(streams):
                    for  stream in streams:
                        api_stream_return = {}
                        for i , component in enumerate(list(stream)):
                            if i == 0:
                                api_stream_return["id"] = component
                                streamid = component
                            elif i == 1:
                                api_stream_return["deviceId"] = component
                            elif i == 2:
                                api_stream_return["key"] = component
                            elif i == 3:
                                api_stream_return["label"]= component
                            elif i == 4:
                                api_stream_return["unitId"] = component
                            elif i == 6:
                                api_stream_return["measurementCount"] = component
                                api_stream_return["measurements"] = []
                                user_device_api_return[0]["streams"].append(api_stream_return)
                            else:
                                continue
                        #adicionando o monitoramento de temperatura ao json (mensurements)
                        streamdata = self.findAllInARow("streamdata","DataStreamID",streamid)
                        if streamdata != False:
                            streamdata = self.findAllInARow("streamdata","DataStreamID",streamid)[-5:]
                            for streamd in streamdata:
                                for idx2,data in enumerate(streamd):
                                    if idx2 == 2:
                                        data_of_stream = {}
                                        data_of_stream["timestamp"]=int(data.timestamp())
                                    elif idx2 == 4:
                                        data_of_stream["value"]=data
                                        api_stream_return["measurements"].append(data_of_stream)

                                    else:
                                        continue
                        


                
                
                #falta iterar e colocar as info no json
                return user_device_api_return
            else:
                return user_device_api_return
            #criar logica de coleta de informações do banco de dados
        except Exception as err:
            logging.error(f"Error in {self.read_user_device.__name__} : {err}")

    

    def read_device_stream(self,streamkey):
        try:
            #criar logica de coleta de informações do banco de dados
            #adicionando as informações das streams ao json (streams)
            device_stream_api_return = []
            streams = self.findAllInARow("devicestream","Akey",streamkey)
            streamid = 0
            if self.shall_not_pass(streams):
                for  stream in streams:
                    api_stream_return = {}
                    for i , component in enumerate(list(stream)):
                        if i == 0:
                            api_stream_return["id"] = component
                            streamid = component
                        elif i == 1:
                            api_stream_return["deviceId"] = component
                        elif i == 2:
                            api_stream_return["key"] = component
                        elif i == 3:
                            api_stream_return["label"]= component
                        elif i == 4:
                            api_stream_return["unitId"] = component
                        elif i == 6:
                            api_stream_return["measurementCount"] = component
                            api_stream_return["measurements"] = []
                            device_stream_api_return.append(api_stream_return)
                        else:
                            continue
                
                    #adicionando o monitoramento de temperatura ao json (mensurements)
                    streamdata = self.findAllInARow("streamdata","DataStreamID",streamid)
                    if streamdata != False:
                        streamdata = self.findAllInARow("streamdata","DataStreamID",streamid)[-5:]
                        for streamd in streamdata:
                            for idx2,data in enumerate(streamd):
                                if idx2 == 2:
                                    data_of_stream = {}
                                    data_of_stream["timestamp"]=int(data.timestamp())
                                elif idx2 == 4:
                                    data_of_stream["value"]=data
                                    api_stream_return["measurements"].append(data_of_stream)

                                else:
                                    continue
                return device_stream_api_return
            else:
                return device_stream_api_return
        except Exception as err:
=======
import mysql.connector
from datetime import datetime
import logging
import uuid 

logging.basicConfig(level=logging.ERROR, format='%(levelname)s %(asctime)s - %(message)s')
#voltar aqui e tratar possiveis erros

class ErrosPersonalizados(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

class CRUD():
    def __init__(self,user:str,password:str,host:str,database:str) -> None:
        self.user = user
        self.password =password
        self.host = host
        self.database = database
        #tratando erros de conexão e informarções erradas com o servidor
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            test_database = f"USE {database};"
            cursor.execute(test_database)

            if None in (user,database,password,host):
                raise ErrosPersonalizados("None type Error")
            
            print(f"++++ Conectado com sucesso a {database} como {user} no host {host} ++++")
            connection.close()
        
        except Exception as err:
            print(f"XXXX user, database, host == {[user,database,host]} XXXX")
            logging.error(f"XXXXX Connection error : {err} XXXXXX")

        #criando key aleatoria com letras e numeros 

    @property    
    def randkey(self):
        return self.__randomKey

    
    
    def shall_not_pass(self,obj):
        """ None and False  shall not pass!!"""
        if obj == False or obj == None:
            return False
        else:
            return True
    
    def findComplex(self,column,table,column1,obj1,column2,obj2):
        """Retorna o ultimo resultado de uma pesquisa no banco usando essa query:
        SELECT {column} FROM {table} WHERE {column1} = '{obj1}' AND {column2} = '{obj2}';"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            query_finder = f"SELECT {column} FROM {table} WHERE {column1} = '{obj1}' AND {column2} = '{obj2}';"
            cursor.execute(query_finder)
            result = cursor.fetchall()
            if self.shall_not_pass(result) and len(result) > 0:
                finder_result = result[-1][0]
                connection.close()
                return finder_result
            else:
                connection.close()
                return False
        except Exception as err:
            logging.error(f"Error in {self.findComplex.__name__} : {err}")

    def findFirstOne(self,column,table,column1,obj):
        """Procura um iten especifico em uma tabela com essa query:\n
            SELECT {column} FROM {table} WHERE {column2} = '{obj}';"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            query_finder = f"SELECT {column} FROM {table} WHERE {column1} = '{obj}';"
            cursor.execute(query_finder)
            result = cursor.fetchone()
            if self.shall_not_pass(result) and len(result) > 0:
                finder_result = result[0]
                connection.close()
                return finder_result
            else:
                connection.close()
                return False
        except Exception as err:
            logging.error(f"Error in {self.findFirstOne.__name__} : {err}")
        
    
    def findAllInARow(self,table,column2,obj):
        """Procura uma row especifica em uma tabela com essa query:\n
            SELECT * FROM {table} WHERE {column2} = '{obj}';"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            query_finder = f"SELECT * FROM {table} WHERE {column2} = '{obj}';"
            cursor.execute(query_finder)
            result = cursor.fetchall()
            if self.shall_not_pass(result) and len(result) > 0:
                connection.close()
                return result
            else:
                connection.close()
                return False
        except Exception as err:
            logging.error(f"Error in {self.findAllInARow.__name__} : {err}")
        
    
    def insert(self,tabela:str,columnList:str,valueList:list):
        """Insere itens em uma tabela com essa query:\n
           INSERT INTO {tabela} {columnList} VALUES {lista_de_valores};"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            retira_colchetes = lambda x: str(x).replace("[","(").replace("]",")")
            lista_de_valores = retira_colchetes(valueList)
            insert_device_information =f"INSERT INTO {tabela} {columnList} VALUES {lista_de_valores};"
            cursor.execute(insert_device_information)
            connection.commit()
            connection.close()
            return True
        except Exception as err:
            logging.error(f"Error in {self.insert.__name__} : {err}")
       
    
    def update(self,table:str,column1:str,value1,whereColumn:str,whereValue):
        """Atualiza um valor em uma row com essa query:\n
           UPDATE {table} SET {column1} = {value1} WHERE {whereColumn} = {whereValue};"""
        try:
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            updateQuery = f"UPDATE {table} SET {column1} = {value1} WHERE {whereColumn} = {whereValue}"
            cursor.execute(updateQuery)
            connection.commit()
            connection.close()
            return True
        
        except Exception as err:
            logging.error(f"Error in {self.update.__name__} : {err}")
    
    
    def create_new_device(self,user:str,label:str,description:str):
        try:
            #gerando key aleatoria
            randkey_new_device = f"{uuid.uuid4()}".replace("-","")
            #find user id
            userid = self.findFirstOne("userId","user","name",user)
            if userid != False:
                #inserindo dados na tabela
                self.insert("sensordevice","(Akey,label,user_userId,description)",[f'{randkey_new_device}',f'{label}',userid,f'{description}'])
                #pegando id do device
                device_id = self.findFirstOne("SensorDeviceID ","sensordevice","Akey",randkey_new_device)
                #retorno Pra api
                device_api_return = [{"id":device_id,"key":randkey_new_device,"label":label,"description":description}]
                return device_api_return
            else:
                return False
        except Exception as err:
            logging.error(f"Error in {self.create_new_device.__name__} : {err}")

   
    def create_new_stream(self,sensorKey:str,label:str,unitId:int):
        try:
            #registro no banco de dados
            randkey_new_device = f"{uuid.uuid4()}".replace("-","")
            sensorid = self.findFirstOne("SensorDeviceID","sensordevice","Akey",sensorKey)
            if self.shall_not_pass(sensorid):
                valueList = [sensorid,randkey_new_device,label,unitId,0,0]
                self.insert("devicestream","(SensorDeviceID,Akey,label,MensurementUnitID,anabled,mensurementCount)",valueList=valueList)
                streamid = self.findFirstOne("DataStreamID","devicestream","Akey",randkey_new_device)
                mensurementcount = self.findFirstOne("mensurementCount","devicestream","Akey",randkey_new_device)
                #retorno Pra api
                strem_api_return = [{"id":streamid,"key":randkey_new_device,"label":label,"unitId":unitId,"deviceId":sensorid,"meansurementCount":mensurementcount}]
                return strem_api_return
            else:
                return False
            
        except Exception as err:
            logging.error(f"Error in {self.create_new_stream.__name__} : {err}")

        
    
    def create_new_stream_data(self,streamKey:str,timeStamp:int,value:float):
        try:
            #registro no banco de dados
            mensurementUnitId = self.findFirstOne("MensurementUnitID","devicestream","Akey",streamKey)
            streamId = self.findFirstOne("DataStreamID","devicestream","Akey",streamKey)
            mensurementcount = self.findFirstOne("mensurementCount","devicestream","Akey",streamKey)
            anabled = self.findFirstOne("anabled","devicestream","Akey",streamKey)
            if not False in (mensurementUnitId,streamId):
                valuelist = [streamId,timeStamp,mensurementUnitId,value]
                self.insert("streamdata","(DataStreamID,TimeStamp,MensurementUnitID,value)",valueList=valuelist)
                stream_data_id = self.findComplex("ID","streamdata","TimeStamp",timeStamp,"DataStreamID",streamId)
                #dar update no mensurament count and anabled
                plus_mensurement_count = mensurementcount+1
                #verifica e habilita o dispositivo
                if anabled == 0:
                    trueAnabled = 1
                    self.update("devicestream","anabled",trueAnabled,"DataStreamID",streamId)
                #retorno Pra api
                new_time_stamp = int(datetime.now().timestamp())
                stream_data_api_return = [{"id":stream_data_id,"timeStamp":new_time_stamp,"value":value,"unitId":mensurementUnitId}]
                self.update("devicestream","mensurementCount",plus_mensurement_count,"DataStreamID",streamId)
                return stream_data_api_return
            else:
                return False
        except Exception as err:
            logging.error(f"Error in {self.create_new_stream_data.__name__} : {err}")
        
    
    def read_mensurement_units(self):
        try:
            #criar logica de coleta de informações do banco de dados
            connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            cursor = connection.cursor()
            cursor.execute("select * from mensurementunit;")
            get_all = cursor.fetchall()
            if get_all != None and len(get_all) > 0:
                mensurament_units_api_return = [{}]
                for index,iten in enumerate(get_all):
                    mensurament_units_api_return.append({})
                    for i,unit in enumerate(iten):
                        if i == 0:
                            mensurament_units_api_return[index]["id"] = unit
                        elif i == 1:
                            mensurament_units_api_return[index]["symbol"] = unit
                        elif i == 2:
                            mensurament_units_api_return[index]["description"] = unit
                        else:
                            continue
                    
                mensurament_units_api_return.pop(-1)
                return mensurament_units_api_return
            else:
                return False
            
        except Exception as err:
            logging.error(f"Error in {self.read_mensurement_units.__name__} : {err}")
        
    
    def read_user_devices(self,user):
        try:
            #criar logica de coleta de informações do banco de dados
            user_devices_api_return = [{}]
            userid = self.findFirstOne("userId","user","name",user)
            devices = self.findAllInARow("sensordevice","user_userID",userid)
            if self.shall_not_pass(userid) :

                if self.shall_not_pass(devices):
                    #percorre device 
                    for index,device in enumerate(devices):
                        #pega todas as streams de um device 
                        streams = self.findAllInARow("devicestream","SensorDeviceID",device[0])
                        #cataloga cada device
                        for idx, obj in enumerate(device):
                            if idx == 0:
                                user_devices_api_return[index]["id"]= obj
                            elif idx == 1:
                                user_devices_api_return[index]["key"]= obj
                            elif idx == 2:
                                user_devices_api_return[index]["label"]= obj
                            elif idx == 4:
                                user_devices_api_return[index]["description"]= obj
                                user_devices_api_return[index]["streams"] = []
                                user_devices_api_return.append({})
                            else:
                                continue
                        #cataloga cada stream de um device e adiciona nas streams do device 
                        if streams != False:
                            for stream in streams:
                                api_stream_return = {}
                                for i , component in enumerate(list(stream)):
                                    if i == 0:
                                        api_stream_return["id"] = component
                                    elif i == 1:
                                        api_stream_return["deviceId"] = component
                                    elif i == 2:
                                        api_stream_return["key"] = component
                                    elif i == 3:
                                        api_stream_return["label"]= component
                                    elif i == 4:
                                        api_stream_return["unitId"] = component
                                    elif i == 6:
                                        api_stream_return["measurementCount"] = component
                                        user_devices_api_return[index]["streams"].append(api_stream_return)
                                    else:
                                        continue
                    

                    user_devices_api_return.pop(-1)
                    return user_devices_api_return
                else:
                    return user_devices_api_return
            else:
                return False
        except Exception as err:
            logging.error(f"Error in {self.read_user_devices.__name__} : {err}")

    
    def read_user_device(self,sensorkey):
        try:
            devices = self.findAllInARow("sensordevice","Akey",sensorkey)
            deviceid=0
            streamid = 0
            user_device_api_return = [{}]
            if self.shall_not_pass(devices):
                #adicionando as informações do device ao json
                for index,device in enumerate(devices[0]):
                    if index == 0:
                        user_device_api_return[0]["id"]=  device
                        deviceid = device
                    if index == 1:
                        user_device_api_return[0]["key"]=  device
                        
                    if index == 2:
                        user_device_api_return[0]["label"]= device
                        
                    if index == 4:
                        user_device_api_return[0]["description"]= device
                        user_device_api_return[0]["streams"] = []
                        
                    else:
                        continue
                #adicionando as informações das streams ao json (streams)
                streams = self.findAllInARow("devicestream","SensorDeviceID",deviceid)
                if self.shall_not_pass(streams):
                    for  stream in streams:
                        api_stream_return = {}
                        for i , component in enumerate(list(stream)):
                            if i == 0:
                                api_stream_return["id"] = component
                                streamid = component
                            elif i == 1:
                                api_stream_return["deviceId"] = component
                            elif i == 2:
                                api_stream_return["key"] = component
                            elif i == 3:
                                api_stream_return["label"]= component
                            elif i == 4:
                                api_stream_return["unitId"] = component
                            elif i == 6:
                                api_stream_return["measurementCount"] = component
                                api_stream_return["measurements"] = []
                                user_device_api_return[0]["streams"].append(api_stream_return)
                            else:
                                continue
                        #adicionando o monitoramento de temperatura ao json (mensurements)
                        streamdata = self.findAllInARow("streamdata","DataStreamID",streamid)
                        if streamdata != False:
                            streamdata = self.findAllInARow("streamdata","DataStreamID",streamid)[-5:]
                            for streamd in streamdata:
                                for idx2,data in enumerate(streamd):
                                    if idx2 == 2:
                                        data_of_stream = {}
                                        data_of_stream["timestamp"]=int(data.timestamp())
                                    elif idx2 == 4:
                                        data_of_stream["value"]=data
                                        api_stream_return["measurements"].append(data_of_stream)

                                    else:
                                        continue
                        


                
                
                #falta iterar e colocar as info no json
                return user_device_api_return
            else:
                return user_device_api_return
            #criar logica de coleta de informações do banco de dados
        except Exception as err:
            logging.error(f"Error in {self.read_user_device.__name__} : {err}")

    

    def read_device_stream(self,streamkey):
        try:
            #criar logica de coleta de informações do banco de dados
            #adicionando as informações das streams ao json (streams)
            device_stream_api_return = []
            streams = self.findAllInARow("devicestream","Akey",streamkey)
            streamid = 0
            if self.shall_not_pass(streams):
                for  stream in streams:
                    api_stream_return = {}
                    for i , component in enumerate(list(stream)):
                        if i == 0:
                            api_stream_return["id"] = component
                            streamid = component
                        elif i == 1:
                            api_stream_return["deviceId"] = component
                        elif i == 2:
                            api_stream_return["key"] = component
                        elif i == 3:
                            api_stream_return["label"]= component
                        elif i == 4:
                            api_stream_return["unitId"] = component
                        elif i == 6:
                            api_stream_return["measurementCount"] = component
                            api_stream_return["measurements"] = []
                            device_stream_api_return.append(api_stream_return)
                        else:
                            continue
                
                    #adicionando o monitoramento de temperatura ao json (mensurements)
                    streamdata = self.findAllInARow("streamdata","DataStreamID",streamid)
                    if streamdata != False:
                        streamdata = self.findAllInARow("streamdata","DataStreamID",streamid)[-5:]
                        for streamd in streamdata:
                            for idx2,data in enumerate(streamd):
                                if idx2 == 2:
                                    data_of_stream = {}
                                    data_of_stream["timestamp"]=int(data.timestamp())
                                elif idx2 == 4:
                                    data_of_stream["value"]=data
                                    api_stream_return["measurements"].append(data_of_stream)

                                else:
                                    continue
                return device_stream_api_return
            else:
                return device_stream_api_return
        except Exception as err:
>>>>>>> ea07eb993347774717500adde3f992bb2f12bf68
            logging.error(f"Error in {self.read_device_stream.__name__} : {err}")