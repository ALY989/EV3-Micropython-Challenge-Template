from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


m.startup()

# Train
@test_decorator
def run():

    m.straight(300)
    m.turn(-110)
    m.straight(630)
    m.turn(110)
    m.straight(450)
    m.straight(-50)
    m.turn(90)
    m.straight(300)
    m.turn(90)
    m.straight(500)
    m.turn(-90)
    m.straight(20)

if __name__ == "__main__":
    
    run()
