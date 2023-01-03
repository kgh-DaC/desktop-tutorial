import RPi.GPIO as GPIO
import time

PWMA=21
AIN1=20
AIN2=16

GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA,GPIO.out)
GPIO.setup(AIN1,GPIO.out)
GPIO.setup(AIN2,GPIO.out)

L_Motor=GPIO.PWM(PWMA,500)
L_Motor.start(0)

try:
    while True:
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,2)
        L_Motor.ChangeDutyCycle(100)
        time.sleep(1.0)

        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        L_Motor.ChangeDutyCycle(0)
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()