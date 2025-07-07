#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
murci = UltrasonicSensor(Port.S1)
mA = Motor(Port.A)
mD = Motor(Port.D)
ev3.speaker.beep()

while True:
    distancia = murci.distance()
    mA.run(300)
    ev3.light.on(Color.GREEN)
    if distancia <= 230:
        ev3.screen.print("Obstáculo detectado:")
        print(distancia/10, "cm")
        wait(200)
        while True:
            distancia = murci.distance()
            ev3.light.on(Color.RED)
            mA.brake()
            mD.brake()
            if distancia <= 130:
                ev3.speaker.beep(frequency=500, duration=100)
                wait(400)