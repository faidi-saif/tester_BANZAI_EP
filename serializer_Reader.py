from serializer import *
from params import *
import threading
import time



class serializer_Reader(serializer):

    def __init__(self,arg_port,arg_baude_rate,arg_name):

        super().__init__(arg_port,arg_baude_rate,arg_parity=PARITY_NONE,arg_stopbits=STOPBITS_ONE)
        self.mthread_name = arg_name
        print("****************************************",self.mthread_name," serializer Init ")
        self.mthread_target = self.ReadData
        self.mthread = threading.Thread(name=self.mthread_name,target=self.mthread_target)
        self.thread_exit_flag = False
        self.m_data=""
        self.coded_data = []
        self.name=arg_name
        #self.mthread.start()
        # '/dev/ttyUSB1'



    def ReadData(self):
        print("thread for ",self.mthread_name," started ")
        self.cleanData()
        while self.thread_exit_flag == False:
            len_data = self.ser.inWaiting()
            if len_data !=0:
                data = self.ser.read(len_data)
                self.coded_data.append(data)
                time.sleep(0.01)


    def start_acquisition(self):
        self.thread_exit_flag = False
        self.mthread = threading.Thread(name=self.mthread_name, target=self.mthread_target)
        self.mthread.start()



    def getData(self):
        self.m_data =""
        for line in self.coded_data:
             self.m_data =self.m_data+ line.decode('utf-8')
        return self.m_data



    def cleanData(self):
        self.m_data = ""
        self.coded_data.clear()


    def stop_acquisition(self):
        self.thread_exit_flag =True
        self.mthread.join()
        print("thread for ",self.mthread_name," STOPPED ")



    def __del__(self):
        #threading.enumerate()
        super().__del__()


