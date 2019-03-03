from node_modules import robot
import time

if __name__=="__main__":

    rob = robot.Robot()
    rob.setAntenna(0x08,1)

    x=0
    while(x<12):
        head=rob.ant.getHeading()
        print(head)
        x+=1
        time.sleep(2)
