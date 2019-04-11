from node_modules import stepperMotor
import time

m1 = stepperMotor.Motor()

m1.forward(1)
time.sleep(4)

m1.backward(1)
time.sleep(4)


m1.disconnect()
