#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

ev3 = EV3Brick()
gancho_motor = Motor(Port.A)
codo_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 50])
base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
codo_motor.control.limits(speed=60, acceleration=120)
base_motor.control.limits(speed=60, acceleration=120)
base_switch = TouchSensor(Port.S1)
codo_sensor = ColorSensor(Port.S3)

codo_motor.run_time(-30, 1000)
codo_motor.run(15)
while codo_sensor.reflection() < 32:
    wait(10)
codo_motor.reset_angle(0)
codo_motor.hold()

base_motor.run(-60)
while not base_switch.pressed():
    wait(10)
base_motor.reset_angle(0)
base_motor.hold()

gancho_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gancho_motor.reset_angle(0)
gancho_motor.run_target(200, -90)


def robot_agarra(position):
    base_motor.run_target(60, position)
    codo_motor.run_target(60, -40)
    gancho_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    codo_motor.run_target(60, 0)


def robot_suelta(position):
    base_motor.run_target(60, position)
    codo_motor.run_target(60, -40)
    gancho_motor.run_target(200, -90)
    codo_motor.run_target(60, 0)

for i in range(3):
    ev3.speaker.beep()
    wait(100)

IZQUIERDA = 160
MEDIO = 100
DERECHA = 40

while True:
    robot_agarra(IZQUIERDA)
    robot_suelta(MEDIO)

    robot_agarra(DERECHA)
    robot_suelta(IZQUIERDA)

    robot_agarra(MEDIO)
    robot_suelta(DERECHA)