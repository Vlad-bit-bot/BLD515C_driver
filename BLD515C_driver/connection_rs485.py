import minimalmodbus
from register_dictionary import *
default_port = '/dev/ttyUSB0'

class Connection:
    def __init__(self, port_name, address, reversed):
        try:
            self.driver = minimalmodbus.Instrument(port_name, address)
            self.driver.serial.baudrate = 9600
            self.driver.serial.bytesize = 8
            self.driver.serial.stopbits = 1
            self.driver.serial.timeout = 0.045
            self.driver.close_port_after_each_call = False
            self.driver.serial.parity = minimalmodbus.serial.PARITY_NONE
            self.driver.mode = minimalmodbus.MODE_RTU
            self.driver.clear_buffers_before_each_transaction = False
            self.port_name = port_name
            self.address = address
            print(f"Driver on {self.port_name} at address {address} connected!")
            self.reversed = reversed

        except Exception as e:
            print(f"Connection error on {port_name}; Error: {e}")
            exit()
   ################################
   #                             #
   #   Interaction with driver   #
   #                             #
   ###############################

    def read_03(self, reg):
        return self.driver.read_register(reg, functioncode=3)
    def write_06(self, reg, val):
        self.driver.write_register(reg, val, functioncode=6)

    def error(self, e, name):
        print(f"Error in {name}! {e}")

    def close_port(self):
        self.driver.serial.close()
        print("Port closed!")

    def save(self):
        try:
            self.write_06(REG_SAVE, SAVE_COMMAND)
        except Exception as e:
            self.error(e, f"save {self.address}")
    def error(self, e, name):
        print(f"Error in {name}! {e}")

    #################################
    #                               #
    #   Telemetry data functions    #
    #                               #
    #################################

    # Function used for reading voltage
    def read_voltage(self):
        try:
            voltage = self.read_03(REG_VOLTAGE_GET)
            return voltage / 10
        except Exception as e:
            self.error(e, "read_voltage")
    # Function used for reading current
    def read_current(self):
        try:
            current = self.read_03(REG_CURRENT_GET)
            return current / 40
        except Exception as e:
            self.error(e, "read_current")
    # Funtion used for reading temperature
    def read_temp(self):
        try:
            temp = self.read_03(REG_TEMP_GET)
            return temp
        except Exception as e:
            self.error(e, "read_temp")
    def read_error(self):
        try:
            code = int(self.read_03(REG_ALARM))
            print(f"{ALARM_CODES.get(code, "Unknown error in read_error")}")
        except Exception as e:
            self.error(e, "read_error")

    #####################################
    #                                   #
    #   Basic motor control functions   #
    #                                   #
    #####################################

    # Function used for setting motor speed
    def set_motor_speed(self, rpm):
        try:
            self.write_06(REG_COMM_SPEED_SET, rpm)
        except Exception as e:
            self.error(e, f"set_motor_speed {rpm}")
    # Function used for turning on the motor
    def start(self):
        try:
            start_command_value = 0x0701  # 07 working mode, 01 start, no brakes, reverse
            self.write_06(REG_CONTROL_STATUS, start_command_value)
        except Exception as e:
            self.error(e,"start")
    # Function used for turning off the motor
    def stop(self, brakes):
        try:
            if(brakes):
                 stop_command_value = CMD_BRAKE_STOP
            else:
                 stop_command_value = CMD_NATURAL_STOP  # natural stop
            self.write_06(REG_CONTROL_STATUS, stop_command_value)
        except Exception as e:
            self.error(e, "stop")
    # Function used for switching direction, 1 forward, 0 backward
    def setDirection(self, bit):
        try:
            command_value = 0x0701 ^ ((bit^self.reversed) << 1)
            self.write_06(REG_CONTROL_STATUS, command_value)
        except Exception as e:
            self.error(e, "setDirection")

    def setAcceleration(self, accel, decel):
        try:
            regVal = ((int(accel))<<8)|(int(decel/10))
            self. write_06(REG_SET_ACCELERATION, regVal)
            self.save()
        except Exception as e:
            self.error(e, "setAcceleration")

