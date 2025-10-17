import math
from machine import Pin, PWM
from time import sleep
import time

#Define pins for motor control

in1 = Pin(11, Pin.OUT)  
in2 = Pin(12, Pin.OUT)  
ena = PWM(Pin(10))     
ena.freq(1000)

in3 = Pin(14, Pin.OUT)  
in4 = Pin(15, Pin.OUT)  
enb = PWM(Pin(13))     
enb.freq(1000) # set PWM frequency

#algorithm to approximate duty cycle required to achieve a wheel speed in radians per s

def get_duty_cycleA(rad_pers): 
    
     max_val = 1 / 0.237122 
     rad_pers = min(rad_pers, max_val)
     duty_cycle = 77202.03 - 78346.63 * math.sqrt(1 - 0.237122 * rad_pers)
     return duty_cycle

def get_duty_cycleB(rad_pers):#didn't end up using this conversion
    
     max_val = 1 / 0.2518919755883
     rad_pers = min(rad_pers, max_val)
     duty_cycle = 113149.072605887 - 112316.91139 * math.sqrt(1-0.2518919755883*rad_pers)
     return duty_cycle
    
#values

drive_forward_speed = int(get_duty_cycleA(100)) #you decide
rotate_speed = 60000  
rotation_time_pdeg = (0.92/180) #s/deg when rotating at specified speed(actually duty cycle) in line above  (empirically determined)



#spin wheels with duty cycle(allowing for negatives to mean reverse direction)
#wheels move when the 2 ins are different, and which is which will simply reverse direction

def spin_motorA(duty_cycle):
    
    if duty_cycle > 0:
        in1.low()
        in2.high()
        ena.duty_u16(duty_cycle)
    else:
        in1.high()
        in2.low()
        ena.duty_u16(abs(duty_cycle))

    
def spin_motorB(duty_cycle):
    
    if duty_cycle > 0:
        in3.low()
        in4.high()
        enb.duty_u16(duty_cycle)
    else:
        in3.high()
        in4.low()
        enb.duty_u16(abs(duty_cycle))    
    
#set both in1 and in2 - or 3 and 4 - to low or high to stop
def stop():
    in1.low()
    in2.low()
    ena.duty_u16(10000)
    
    in3.low()
    in4.low()
    enb.duty_u16(10000)
    

current_angle = 180 # because it starts out pointing to 180


#this is the main function to move it
def move(target_angle):
    global current_angle
    
    print(f"Current angle: {current_angle}°")
    
    # calculate shortest rotation needed
    angle_diff = target_angle - current_angle
    
    # shortest path (-180 to 180)
    if angle_diff > 180:
        angle_diff -= 360
    elif angle_diff < -180:
        angle_diff += 360
    
    if angle_diff != 0:
        print(f"rotating {abs(angle_diff)}°...")
        
        rotation_time = abs(angle_diff) * rotation_time_pdeg
        
        # rotate (accounts for direction)
        if angle_diff > 0:
            spin_motorB(rotate_speed)  
        else:
            spin_motorB(-rotate_speed)  
            
        sleep(rotation_time)
        stop()
        
        # update current angle
        current_angle = target_angle
    
    print("moving")
    
    spin_motorA(drive_forward_speed)
    sleep(0.5)
    stop()
    
    print(f"New current angle: {current_angle}°")
        
    
    
    
        
    
    

angle = 0

while True:
    angle = int(input("Enter angle: "))
    move(angle)
    sleep(0.2)
    stop()
    sleep(0.1)
    
    
#README
"""
idkidkdiekdidek
"""
