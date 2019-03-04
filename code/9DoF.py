from smbus2 import SMBusWrapper
import time

if __name__=="__main__":
    add = 0x1E
    reg = 0x2A

    while True:
        with SMBusWrapper(1) as bus:
            data = bus.read_i2c_block_data(add,reg,2)
            print("Y heading Low: "+data)

        time.sleep(1)
