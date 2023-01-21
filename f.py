
import paho.mqtt.client as mqtt #import the client1
import time
import RPi.GPIO as GPIO          
import time 
in1 = 23
in2 = 24
ena = 25

in3 = 5
in4 = 6
enb = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p=GPIO.PWM(ena,1000)
p1=GPIO.PWM(enb,1000)




def on_message(client, userdata, message):
    print(message.payload.decode("utf-8"))
    if(message.payload.decode("utf-8") == "ON"):
        print("run")
        p.start(50)
        p1.start(50)
        
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    
        time.sleep(5)
        
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)   
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        time.sleep(5)
   
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        time.sleep(5)

        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

        time.sleep(5)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

    if(message.payload.decode("utf-8") == "ONaa"):
        print("runhhhhhhh")
        p.stop()
        p1.stop()

   

broker_address="broker.hivemq.com"
port = 1883
print("creating new instance")
client = mqtt.Client("P4") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address,port,keepalive=60) #connect to broker

print("Subscribing to topic","spbot")
client.subscribe("spbot")

client.loop_forever() #stop the loop
