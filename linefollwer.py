from wpilib import DigitalInput

class LineFollower:
    def __init__(self, drivetrain):
        self.left_sensor = DigitalInput(8)
        self.right_sensor = DigitalInput(9)
        self.drivetrain = drivetrain

    def run(self):
        left_data = self.left_sensor.get()
        right_data = self.right_sensor.get()
        if left_data == 1:
            self.drivetrain.move(1, 10)
        elif right_data == 1:
            self.drivetrain.move(1, -10)
        elif left_data == 1 & right_data == 1:
            self.drivetrain.move(0, 90)
        else:
            self.drivetrain.move(1, 0)
