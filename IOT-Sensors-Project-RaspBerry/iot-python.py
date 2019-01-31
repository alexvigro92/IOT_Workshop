import os, json
import ibmiotf.application
import uuid
import time
from datetime import datetime
import sys
import Adafruit_DHT
import thread

client = None
data = {}

def myCommandCallback(cmd):
    if cmd.event == "event":
        payload = json.loads(cmd.payload)
        

def getDataFromSensor():
    global data
    humidityBefore, temperatureBefore = Adafruit_DHT.read_retry(11, 4)
    while 1:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        #print humidity
        #print temperature
        if((humidity - humidityBefore) > 30):
            temperature = temperatureBefore
            humidity = humidityBefore
            data['temp'] = str(temperature)
            data['hum'] = str(humidity)
        else:
            humidityBefore = humidity
            temperatureBefore = temperature
            data['temp'] = str(temperature)
            data['hum'] = str(humidity)


try:
    thread.start_new_thread(getDataFromSensor, ( ))
    options = ibmiotf.application.ParseConfigFile("/home/pi/Desktop/iot_TempHum/device.cfg")
    options["deviceId"] = options["id"]
    options["id"] = "aaa" + options["id"]
    client = ibmiotf.application.Client(options)
    client.connect()
    client.deviceEventCallback = myCommandCallback
    client.subscribeToDeviceEvents(event="event")
    count = 0
    while True:
        
        data['date'] = str(datetime.now().strftime('%Y-%m-%d'))
        data['time'] = str(datetime.now().strftime('%H:%M:%S'))
        client.publishEvent("raspberrypi", options["deviceId"], "event", "json", data)
        print data
        time.sleep(5)
        
except ibmiotf.ConnectionException  as e:
    print e
