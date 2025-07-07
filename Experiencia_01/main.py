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
    mD.run(300)
    
    if distancia <= 230:
        ev3.screen.print("Obstáculo detectado:")
        print(distancia/10, "cm")
        wait(200)
        mA.brake()
        mD.brake()
        wait(500)
        mA.run(300)
        wait(1300)

