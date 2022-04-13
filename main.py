#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Use the following links to access the documentation
# How to control the EV3: https://docs.pybricks.com/en/v2.0/hubs.html#pybricks.hubs.EV3Brick
# Robot motors and sensors: https://docs.pybricks.com/en/v2.0/ev3devices.html
# How to implement timing and logging in your program: https://pybricks.com/ev3-micropython/tools.html
# Control robot using the robot object https://pybricks.com/ev3-micropython/robotics.html
# Rule book: https://firstinspiresst01.blob.core.windows.net/first-forward/fll-challenge/fll-challenge-cargo-connect-robot-game-rulebook.pdf

import mission, mission1, mission2, mission3, mission4, mission5, mission6, mission7, mission8, mission9, mission10, mission11, mission12, mission13, mission14, mission15, mission16, mission17, mission18, mission19

# Create your objects here.
ev3 = EV3Brick()
# Startup
ev3.speaker.beep()
ev3.screen.print("%s Beginning..." %__name__)

# Reorder the missions here to the order you want them to run. 
# Pass in more parameters to the run function if you need them.
mission1.run()
mission2.run()
mission3.run()
mission4.run()
mission5.run()
mission6.run()
mission7.run()
mission8.run()
mission9.run()
mission10.run()
mission11.run()
mission12.run()
mission13.run()
mission14.run()
mission15.run()
mission16.run()
mission17.run()
mission18.run()
mission19.run()
mission20.run()
