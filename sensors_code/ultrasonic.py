from machine import Pin
import utime
import time

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def get_distance_cm(trigger: Pin, echo: Pin):
    """
    Gets the distance from the HC-SR04 in cm.

    Args:
        trigger (Pin): Should be set to Pin.OUT and the same IO pin attached to trigger
        echo (Pin): Set to Pin.IN and the same IO pin connected to echo

    Returns:
        float: In cms of distance from the ultrasonic sensor
    """
    trigger.low()
    utime.sleep_us(2)   
    trigger.high()
    utime.sleep_us(5)
    trigger.low

    while echo.value() == 0:
        signaloff = utime.ticks_us()
        
    while echo.value() == 1:
       signalon = utime.ticks_us()

    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2

    return distance


while True:
    print(get_distance_cm())
    time.sleep(1)