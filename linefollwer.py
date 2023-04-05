from wpilib import DigitalInput

class LineFollower:
    def __init__(self, drivetrain):
        self.left_sensor = DigitalInput(9)
        self.right_sensor = DigitalInput(8)
        self.drivetrain = drivetrain

    def run(self):
        left_data = self.left_sensor.get()
        right_data = self.right_sensor.get()
        print(left_data, right_data)
        if left_data and not right_data:
            print("leftREAD")
            self.drivetrain.move(-0.5, 0.4)
        elif right_data and not left_data:
            print("rightREAD")
            self.drivetrain.move(0.5, 0.4)
        else:
            print("bothREAD")
            self.drivetrain.move(0, 0.4)
