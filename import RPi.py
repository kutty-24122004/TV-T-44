import RPi.GPIO as GPIO
from mfrc522 import SimpleMFR522
from time import sleep

#physical pin no GPI023 is 16
buzzer=16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer,GPIO.OUT)
reader=simpleMFRC522()
s_list={
            150600874571:["Vijaya",405],
            222317692363:["Shirisha",413],
            907345986202:["Akshitha",410],
}
last_id=0
print("Initialization Complete...............")
while True:
        try:
                id, text = reader.read()
                if(lasr_id !=id):
                        GPIO.output(buzzer,GPIO.HIGH)
                        print(s_list[id][1],"   ",s_list[id][0],"   Present")
                        sleep(0,1)
                        GPIO.output(buzzer,GPIO.LOW)
                     else:
                        print("Warning: Not a Registered Card - id no:",id)
                        pass
                last_id = id
                expect:
                      print("existing program")
                      sleep(3)   