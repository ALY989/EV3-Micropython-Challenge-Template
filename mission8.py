from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from mission import test_decorator
import mission as m
import debug as d


m.startup()

# Train
@test_decorator
def run():

    d.straight(300)
    d.turn(-110)
    d.straight(630)
    d.turn(110)
    d.straight(450)
    d.straight(-50)
    d.turn(90)
    d.straight(300)
    d.turn(90)
    d.straight(500)
    d.turn(-90)
    d.straight(20)

if __name__ == "__main__":
    
    run()
