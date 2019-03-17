from smbus2 import SMBusWrapper
from node_modules import DoF
import time

if __name__=="__main__":
    D = DoF.DoF()

    D.magRead()

    while True:
        print(D.getHeading())
        time.sleep(1)
