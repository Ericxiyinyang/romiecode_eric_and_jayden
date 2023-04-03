import wpilib as wp
import wpilib.drive as drive
class DriveTrain:
    def __init__(self):
        self.left_motor = wp.Spark(0)
        self.right_motor = wp.Spark(1)
        self.drivetrain = drive.DifferentialDrive(self.left_motor, self.right_motor)

    def move(self, forward, rotate):
        self.drivetrain.arcadeDrive(forward, rotate)