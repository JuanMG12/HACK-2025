# from connections import connect_mqtt, connect_internet
# from time import sleep


# def main():
#     try:
#         connect_internet("",password="") #ssid (wifi name), pass
#         client = connect_mqtt("", "", "") # url, user, pass

#         while True:
#             client.check_msg()
#             sleep(0.1)

#     except KeyboardInterrupt:
#         print('keyboard interrupt')
        
        
# if __name__ == "__main__":
#     main()

from machine import Pin
import time

# The onboard LED is on GPIO 25
led = Pin("LED", Pin.OUT)

while True:
    led.on()          # Turn LED on
    time.sleep(0.5)   # Wait 0.5 seconds
    led.off()         # Turn LED off
    time.sleep(0.5)   # Wait 0.5 seconds

