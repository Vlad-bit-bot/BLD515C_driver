# run this RIGHT NOW as a standalone script
import minimalmodbus

def save_at_57600(address):
    d = minimalmodbus.Instrument('/dev/ttyUSB0', address)
    d.serial.baudrate = 57600
    d.serial.bytesize = 8
    d.serial.stopbits = 1
    d.serial.parity   = minimalmodbus.serial.PARITY_NONE
    d.serial.timeout  = 0.05
    d.mode            = minimalmodbus.MODE_RTU
    d.clear_buffers_before_each_transaction = False
    d.close_port_after_each_call = False
    try:
        d.write_register(33279, 65535, functioncode=6)
        print(f"Address {address} saved!")
    except Exception as e:
        print(f"Address {address} failed: {e}")

save_at_57600(1)
save_at_57600(2)
