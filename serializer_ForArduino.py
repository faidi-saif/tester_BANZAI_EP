from serializer import *
from params import *


class serializer_ForArduino(serializer):

    def __init__(self,arg_port,arg_baude_rate=9600):
        self.mparity = PARITY_NONE
        self.mstopbits = STOPBITS_ONE
        super().__init__(arg_port=arg_port,arg_baude_rate=arg_baude_rate,arg_parity=self.mparity,arg_stopbits=self.mstopbits)
        # '/dev/ttyUSB0'

    def PowerOn(self):  # tested OK!
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(PRESS_POW)
        time.sleep(2)
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(RELEASE_POW)
        time.sleep(2)

    def PowerOff(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(PRESS_POW)
        time.sleep(4)
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(RELEASE_POW)
        time.sleep(2)

    def reinitialise(self):  # tested Ok
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(RE_INIT)
        time.sleep(3)

    def reset(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(PRESS_EP_RST)
        time.sleep(2)
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(RELEASE_EP_RST)
        time.sleep(1.5)

    def fw_flash(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(PRESS_POW)  # press power
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(PRESS_SHUTT)  # press shutter
        time.sleep(10)
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(RELEASE_POW)
        time.sleep(3)
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(RELEASE_SHUTT)
        time.sleep(2)




# m_serialzer = serializer_ForArduino('/dev/ttyUSB0',9600)
# m_serialzer.PowerOn()
# serializer_ForArduino.reinitialise()

# ser=Serial('/dev/ttyUSB0',9600,timeout=None)
# print(ser.portstr)
# ser.close()