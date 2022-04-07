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

import mission1, mission2, mission3, mission4, mission5, mission6, mission7, mission8, mission9, mission10, mission11, mission12, mission13, mission14, mission15, mission16, mission17, mission18, mission19, mission20


# Create your objects here.
ev3 = EV3Brick()
# Startup Beep
ev3.speaker.beep()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# If you want to use more motors, add them here. 
#arm_motor = Motor(Port.A)

# Initialize the drive base. 
# MIGHT WANT TO CHECK TO MAKE SURE THIS IS RIGHT
# axle_track is distance between the two wheels
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

#Initiliaze sensor
ultrasonicSensor = UltrasonicSensor(Port.S1)

# settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration
robot.settings(250, 250, 360, 720)

# Initialize any sensors you want here by uncommenting and changing the port.

#touch_sensor = TouchSensor(Port.S1)
# To use touch sensor, pass it in as a parameter in the run function for whichever mission needs it.
# Example usage:
# def run(robot, touch_sensor):
#     # drive forward until the touch sensor is pressed
#     while !touch_sensor.pressed():
#         robot.drive(100, 0)
#     robot.stop()

#color_sensor = ColorSensor(Port.S2)
# To use color sensor, pass it in as a parameter in the run function for whichever mission needs it.
# Example usage:
# def run(robot, color_sensor):
#     # drive forward until the color sensor sees the color you want
#     while color_sensor.color() != Color.BLACK:
#         robot.drive(100, 0)
#     robot.stop()

#ultrasonic_sensor = UltrasonicSensor(Port.S3)
# To use ultrasonic sensor, pass it in as a parameter in the run function for whichever mission needs it.
# Example usage:
# def run(robot, ultrasonic_sensor):
#     # drive forward until the ultrasonic sensor sees the distance you want
#     while ultrasonic_sensor.distance() > 10:
#         robot.drive(100, 0)
#     robot.stop()

#gyro_sensor = GyroSensor(Port.S4)
# To use gyro sensor, pass it in as a parameter in the run function for whichever mission needs it.
# Example usage:
# def run(robot, gyro_sensor):
#     # turn until the gyro sensor sees the angle you want
#     while gyro_sensor.angle() < 10:
#         robot.drive(0, 100)
#     robot.stop()

def waitUntilButton(button):
    while (not button in ev3.buttons.pressed()):
        wait(10)

# Example to wait until center button is pressed:
# waitUntilButton(Button.CENTER)

# Reorder the missions here to the order you want them to run. 
# Pass in more parameters to the run function if you need them.mission1.run(robot)
mission1.run(ev3, robot, ultrasonicSensor, left_motor, right_motor)
#mission2.run(robot)
#mission3.run(robot)
#mission4.run(robot)
#mission5.run(robot)
#mission6.run(robot)
#mission7.run(robot)
# mission8.run(robot)
#mission9.run(robot)
#mission10.run(robot)
#mission11.run(robot)
#mission12.run(robot)
#mission13.run(robot)
#mission14.run(robot)
#mission15.run(robot)
#mission16.run(robot)
#mission17.run(robot)
#mission18.run(robot)
#mission19.run(robot)
#mission20.run(robot)
