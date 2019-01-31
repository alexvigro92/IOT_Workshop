from cloudant.client import Cloudant
import cloudant as cl
import config as conf


class DBCloudant:

    def __init__(self):
        self.client = ""
        self.session = ""
        self.dataBase = ""
        self.document = ""
        self.query = ""

    def connect(self):
        self.client = Cloudant(conf.username,conf.password,url=conf.url,connect=True)
        self.session = self.client.session()
        if self.session['userCtx']['name']:
            print("Coneccion realizada correctamente")
        else:
            print("Error al conectar con la BD")


    def disconnect(self):
        self.client.disconnect()

    def createDB(self,name):
        try:
            self.dataBase = self.client.create_database(name)
            if self.dataBase.exists():
                print("DB creada correctamente")
        except Exception as error:
            print("DB ya existente")

    def getDataBases(self):
        return self.client.all_dbs()

    def deleteDataBase(self,name):
        return self.client.delete_database(name)

    def openDB(self,name):
        self.dataBase = self.client[name]

    def createDocument(self,data):
        self.document = self.dataBase.create_document(data)
        if self.document.exists():
            print("Se creo el documento correctamente")

    def getDocument(self,name):
        self.document = self.dataBase[name]
        return self.document

    def getAllDocuments(self,name):
        return self.dataBase

    def getDocumentBySensor(self,sensor):
        self.query = cl.query.Query(self.dataBase)
        with self.query.custom_result(selector={"sensor":sensor}) as rst:
            return rst
         






    
