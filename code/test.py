from node_modules import robot

if __name__=="__main__":

    rob = Robot()
    rob.setAntenna(0x08,1)

    x=0
    while(x<12):
        head=rob.ant.getHeading()
        print(head)
        x+=1
