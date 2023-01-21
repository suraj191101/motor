from time import sleep
import os,sys
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
from urllib.parse import urlparse
#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
#DC_Motor_Pin1 = 22                # Define PIN for DC Motor
#DC_Motor_Pin2 = 25                # Define PIN for DC Motor
#GPIO.setup(DC_Motor_Pin1,GPIO.OUT)   # Set pin function as output
#GPIO.setup(DC_Motor_Pin2,GPIO.OUT)   #.3 Set pin function as output

def on_connect(self, mosq, obj, rc):
        #self.subscribe("Fan", 0)
        print("successfully connected")
    
def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if(msg.payload == "on"):    
        print("FAN ON")                        # Give 5 second delay
    else:    
        print("FAN OFF")
       192.168.68.147
def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

    
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

mqttc = paho.Client()                        # object declaration
# Assign event callbacks
mqttc.on_message = on_message                          # called as callback
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe


url_str = os.environ.get('motors_rotate', 'ws://broker.emqx.io:8083') 
url = urlparse(url_str)
print(url.hostname)
print(url.port)
mqttc.connect(url.hostname, url.port)

rc = 0
while True:
    while rc == 0: 
        rc = mqttc.loop()
    print("rc: " + str(rc))
