# led blink and traffic light system
# import the required libraries
from gpiozero import Button, TrafficLights, Buzzer    
from time import sleep    

#buzzer for alarm    
buzzer = Buzzer(15)
button = Button(21)
# pin cofigurations for Traffic Lights (Red,Green,Amber)
lights = TrafficLights(25, 8, 7)    

# iterate the loop statements.   
while True:    
           button.wait_for_press()   
           buzzer.on()   
           light.green.on()    
           sleep(1)    
           lights.amber.on()    
           sleep(1)    
           lights.red.on()    
           sleep(1)    
           lights.off()   
           buzzer.off()
#end of the program
