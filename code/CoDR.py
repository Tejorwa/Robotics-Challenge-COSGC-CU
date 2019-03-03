for node_modules import robot

if __name__=="__main__":

    rob = robot.Robot()
    rob.setAntenna(0x08)

    while True:
        head = rob.ant.getHeading()
        print(head)
