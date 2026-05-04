from connection_rs485 import Connection, default_port  # importing all basic actions
import time
REVERSED = 1
FORWARD = 0

class Controller:

    def __init__(self):
        self.rightMotor = Connection(default_port, 1, REVERSED)
        self.leftMotor = Connection(default_port, 2, FORWARD)
        #self.rightMotor.setAcceleration(200,600)
        #self.leftMotor.setAcceleration(200,600)


    #########################################
    #                                       #
    #   Advanced Movement with joystick     #
    #                                       #
    #########################################

    def changeBaud(self):
        try:
             print(self.rightMotor.read_03(33031))
             print(self.leftMotor.read_03(33031))
            # self.rightMotor.write_06(33031, 24324)
            # self.leftMotor.write_06(33031, 24324)
            # time.sleep(0.5)
            # self.rightMotor.driver.serial.baudrate = 57600
            # self.leftMotor.driver.serial.baudrate  = 57600
            # time.sleep(0.5)
             self.rightMotor.save()
             self.leftMotor.save()
             print("Baud changed — now update baudrate in Connection to 57600 and restart")
        except Exception as e:
             print(f"Baud change failed: {e}")

    # Funtion for setting power (-1 to 1), -100% to 100%
    def setPower(self, right_power: float, left_power: float):
        MAX_SPEED = 3000  # Maximum allowed by the gearbox

        def applyPower(motor, power):
            direction = 1 if power >= 0 else 0
            motor.setDirection(direction)
            return abs(power) * MAX_SPEED

        var1 = applyPower(self.rightMotor, right_power)
        var2 = applyPower(self.leftMotor, left_power)
        self.rightMotor.set_motor_speed(var1)
        self.leftMotor.set_motor_speed(var2)
    def stop(self, brakes):
        self.leftMotor.stop(brakes)
        self.rightMotor.stop(brakes)
    def getTemp(self):
        left_temp = self.leftMotor.read_temp()
        right_temp = self.rightMotor.read_temp()
        if(left_temp!=None and right_temp!=None):
            return (float(left_temp) + float(right_temp)) / 2.0
        else:
            print("Temp is none")
        return 0

    def getCurrent(self):
        left_current = self.leftMotor.read_current()
        right_current = self.rightMotor.read_current()
        if (left_current != None and right_current != None):
            return (float(left_current) + float(right_current)) / 2.0
        else:
            print("Current is none")
        return 0

    def getVoltage(self):
        left_voltage = self.leftMotor.read_voltage()
        right_voltage = self.rightMotor.read_voltage()
        if (left_voltage != None and right_voltage != None):
            return (float(left_voltage) + float(right_voltage)) / 2.0
        else:
            print("Voltage is none")
        return 0
    def printError(self):
        self.leftMotor.read_error()
        self.rightMotor.read_error()
