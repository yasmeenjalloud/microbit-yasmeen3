from microbit import *
from ultrasonic import Ultrasonic

# default pins in Ultrasonic class are:
# trigger: pin13
# echo: pin15

ultrasonic_sensor = Ultrasonic()
# or
# ultrasonic_sensor = Ultrasonic(trig=pin13, echo=pin15)

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    motion = pin1.read_digital()
    if distance_value < 15 and motion == 1:
        add_text(0,0)
    display.scroll(str(int(distance_value)))
    sleep(2000)