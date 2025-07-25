from machine import Pin, ADC
import time


photo_ADC = ADC(Pin(26)) # can change this value for different adc pins

def process_lumens(photoresistor_ADC_pin: ADC) -> float:
    """
    Gets adc value from photoresistor, returns a float for the lumens.
    Assuming to use a 3k ohm resistor in series with the photoresistor
    for the voltage divider. ADC measures voltage relative to ground
    across photoresistor.

    *** prints adc val for now for adjusting of values ***

    Args:
        photoresistor_ADC_pin (ADC): the ADC pin set to read the photresistor voltage

    Returns:
        float: the value of luminosity in lumens
    """

    MAX_ADC = 65000
    ADC_RANGE = MAX_ADC - 1200 # dont change
    adc_val = photo_ADC.read_u16()

    print(f"adc val: {adc_val}", end = "\t")
    lumens = (-adc_val + MAX_ADC)/(ADC_RANGE)
    return lumens

while True:
    print(f"lumen value: {process_lumens(photo_ADC):02f}")
    time.sleep_ms(1000)
    