import Adafruit_BBIO.ADC as ADC
import time

light_sensor = 'P9_37'

ADC.setup()

print('Millivolts')

while True:
    reading = ADC.read(light_sensor)
    millivolts = reading * 1800
    print(millivolts)
    time.sleep(1)
