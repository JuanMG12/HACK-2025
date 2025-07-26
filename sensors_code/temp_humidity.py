from machine import Pin
import dht, time

dht11 = dht.DHT11(Pin(2))
CONST_DIFF_TEMP = 77-71
CONST_DIFF_HUMIDITY = 52 - 61

def get_temp_humidity(dhtpin: dht):
    """
    This gets the temperature and humidity from the dht11.


    Args:
        dhtpin (dht): Any dht object you set the input (middle pin) of
        the dht11 to, needs to be a certain pin in the syntax of 
        'dht.DHT11(Pin(your pin here))'

    Returns:
        array: a two element array, first element containing the temperature
        in Farenheit, and second element containing the humidity in percentage
    """
    dhtpin.measure()
    temp_C = dhtpin.temperature()
    humidity = dhtpin.humidity() - CONST_DIFF_HUMIDITY
    temp_F = temp_C * 9/5 + 32 - CONST_DIFF_TEMP

    temp_humidity_arr = [temp_F, humidity]

    return temp_humidity_arr

while True:
    temp_humidity_arr = get_temp_humidity(dht11)
    print(f"temp: {temp_humidity_arr[0]:.02f}\thumidity: {temp_humidity_arr[1]}%")
    time.sleep(1)
