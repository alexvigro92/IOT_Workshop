import os,json
from flask import Flask, jsonify
import ibmiotf.device
import ibmiotf.application
from ibmiotf import *
import urllib

client = None
dato = []
cad = ""
datos = []

deviceId = os.getenv("DEVICE_ID")

print deviceId

def myCommandCallback(event):
    global dato
    dato.append(event.payload)

def getJson():
    if(len(dato) != 0):
        datos = dato.pop(0)
        return datos


def startConnection():
	try :
		option = {
                "org" : "",
                "id" : "",
                "domain": "",
                 "auth-method" : "apikey",
                "auth-key" : "",
                "auth-token" : ""
		}
		client = ibmiotf.application.Client(option)
		client.connect()
		print "conectado"
		client.deviceEventCallback = myCommandCallback
		client.subscribeToDeviceEvents(event="event",msgFormat="json")
	except ibmiotf.ConnectionException as e:
		print "error mensaje"
		print e
		return e


app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return app.send_static_file('sensors.html')

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

@app.route('/api/raspberry')
def GetTemp():
    return jsonify(results=getJson())


port = os.getenv('PORT', '8000')
if __name__ == "__main__":
	app.secret_key = "minombre"
	startConnection()
	app.run(host='0.0.0.0', port=int(port),use_reloader=False)
