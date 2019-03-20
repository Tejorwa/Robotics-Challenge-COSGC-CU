from node_modules import sonicSensor
import time

if __name__=="__main__":

    sonic = sonicSensor.sonicSensor()

    while True:
        print(sonic.ping())
        time.sleep(1)
