from smbus2 import SMBusWrapper
from node_modules import DoF
import time

if __name__=="__main__":
    D = DoF.DoF(0x1E)

    while True:
        print(D.getHeading())
        time.sleep(1)
