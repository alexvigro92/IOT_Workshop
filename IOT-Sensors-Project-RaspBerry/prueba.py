import DBCloudant as DB
import json
import requests
import config as conf

db = DB.DBCloudant()
db.connect()
##db.createDB('iot_tmp_hum')
##db.deleteDataBase('iot_tmp_hum')
db.openDB('iot_tmp_hum')
##document = {'_id':'4',
##            'sensor':'hum',
##            'value':56}
##db.createDocument(document)
##print db.getDocument('1')
for i in db.getDocumentBySensor("hum"):
    print i

db.disconnect()
