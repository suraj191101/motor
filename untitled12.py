import RPi.GPIO as GPIO
import time
in1 = 17
in2 = 27
en1 = 22
en2 = 25

temp1=1

in3 = 24
in4 = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p=GPIO.PWM(en1,1000)
p1=GPIO.PWM(en2,1000)

p.start(25)
p1.start(25)
print("\n")
print("Enter 'i' for ON and 'o' for OFF")
print("\n")    

while(1):

    x=input()
    
    if x=='i':
        print("run")
        if(temp1==1):
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
          
        

