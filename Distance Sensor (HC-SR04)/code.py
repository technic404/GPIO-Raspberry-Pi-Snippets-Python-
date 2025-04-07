from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24)

while True:
    print(f'Distance {sensor.distance * 100} cm')
    sleep(0.5)