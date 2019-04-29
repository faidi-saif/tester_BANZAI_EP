from serial import *
import time

class serializer:

    def __init__(self,arg_port,arg_baude_rate=9600,arg_parity=None,arg_stopbits = None):
        self.mstopbits = arg_stopbits
        self.mparity=arg_parity
        self.mport = arg_port
        self.mbaudrate =arg_baude_rate # 9600
        self.ser = Serial(port=self.mport,baudrate= self.mbaudrate,parity=self.mparity,stopbits=self.mstopbits,timeout=None)
        print( "Access to ===> ",self.ser.portstr)

        if self.ser.portstr == self.mport:  # check which port is really used
            pass
        else:
            raise Exception("Wrong port or device ! check your usb port")


    def __del__(self):
        self.ser.close()
        # pass