import wpilib as wp
import os
from drivetrain import DriveTrain as DT
from linefollwer import LineFollower as LF
import time

class MyRobot(wp.TimedRobot):
    def robotInit(self):
        '''This method is called as the robot turns on and is often used to setup the
        joysticks and other presets.'''
        self.controller = wp.Joystick(0)
        self.drivetrain = DT()
        self.linefollower = LF(self.drivetrain)

    def robotPeriodic(self):
        '''This is called every cycle of the code. In general the code is loop
        through every .02 seconds.'''
        pass

    def autonomousInit(self):
        '''This is called once when the robot enters autonomous mode.'''
        pass

    def autonomousPeriodic(self):
        '''This is called every cycle while the robot is in autonomous.'''
        while True:
            self.linefollower.run()
            time.sleep(0.3)

    def teleopInit(self):
        '''This is called once at the start of Teleop.'''
        pass

    def teleopPeriodic(self):
        '''This is called once every cycle during Teleop'''
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.move(forward, rotate)

    ### There are other methods that you can overwrite for when the robot is
    # disabled, or when the robot is in Test mode.


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wp.run(MyRobot)
