import RPi.GPIO as GPIO
import time
in1 = 17
in2 = 27
en1 = 22
en2 = 25
in3 = 24
in4 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)


GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

while True:
       GPIO.output(in1,GPIO.HIGH)
       GPIO.output(in2,GPIO.LOW)
       GPIO.output(in3,GPIO.HIGH)
       GPIO.output(in4,GPIO.LOW)
       time.sleep(5)
       GPIO.output(in1,GPIO.HIGH)
       GPIO.output(in2,GPIO.LOW)
       GPIO.output(in3,GPIO.LOW)
       GPIO.output(in4,GPIO.HIGH)
       time.sleep(5)
