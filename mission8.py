from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# To be able to use sensors and control individual motors, make them parameters here
# and pass them to the run function from main.py
# Train
def run(robot):
    robot.straight(200)
    robot.turn(-90)
    robot.straight(600)
    robot.turn(90)
    robot.straight(300)
    robot.straight(-250)
    robot.turn(90)
    robot.straight(300)
    robot.turn(90)
    robot.straight(500)
    robot.turn(-90)
    robot.straight(20)
