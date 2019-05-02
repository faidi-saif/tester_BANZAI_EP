from frw_tester import *
from logger import *
import os
import shutil




class ScenarioMaker:
    def __init__(self):
        self.m_frw_tester = frw_tester()
        self.m_logger = logger()
        self.m_frw_tester.goto_path("/BANZAI_EP")  # redirect you to ~/BANZAI_EP
        self.home_path =self. m_frw_tester.abspath
        self.logs_path = os.environ["HOME"] + "/Logs"  # create a directory for personal logs
        self.checkdir(self.logs_path)  # chek if the Logs directory or not if not create it else nothing will be done
        self.cleandir(self.logs_path)  # delete all directories +files in the logs path

    def reset(self):
        self.m_frw_tester.__del__()
        self.m_frw_tester.__init__()

    def checkdir(self,arg_path):
        if os.path.isdir(arg_path):
            pass
        else:
            os.mkdir(arg_path)



    def cleandir(self,arg_path): # clean previous logs
        for the_file in os.listdir(arg_path):
            file_path = os.path.join(arg_path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

    def __del__(self):
        self.m_frw_tester.__del__()

    def copy_files(self,from_path, to_path):
        if os.path.exists(to_path):
            #self.cleandir(to_path)
            shutil.rmtree(to_path)
        shutil.copytree(from_path, to_path)






    def reset(self):
        self.m_frw_tester.reset_camera()




    def Reset_Test(self):
        loc_path =self.logs_path+"/ResetTest"
        self.checkdir(loc_path)
        self.m_frw_tester.start_acquisition()
        self.m_frw_tester.reset_camera()
        time.sleep(5)
        self.m_frw_tester.stop_acquisition()
        linux_rtos_logs =self.m_frw_tester.get_data()
        self.m_logger.write(loc_path+"/linux_ResetTest_log.txt",linux_rtos_logs[0])
        self.m_logger.write(loc_path+"/rtos_ResetTest_log.txt",linux_rtos_logs[1])



    def Test_video(self,test_mode,flare=1,arg_time=4):
        loc_path = self.logs_path + "/test_video_"+test_mode
        self.checkdir(loc_path)
        self.m_frw_tester.start_acquisition()
        self.m_frw_tester.runTest(still=0,test_mode="5K_EAC_30_W_HEVC_IMX577", flare=flare, time=arg_time)
        time.sleep(5)
        self.m_frw_tester.stop_acquisition()
        linux_rtos_logs = self.m_frw_tester.get_data()
        self.m_logger.write(loc_path + "/linux_"+test_mode+"video_log.txt", linux_rtos_logs[0])
        self.m_logger.write(loc_path + "/rtos_"+test_mode+"video_log.txt", linux_rtos_logs[1])
        self.copy_files(self.home_path+"/Desktop/test_capt",loc_path+"/test_capt")
        self.cleandir(self.home_path + "/Desktop/test_capt")
        time.sleep(1.5)



    def Test_image(self,test_mode="5K_EAC_30_W_HEVC_IMX577",test_option=None):
        loc_path =self.logs_path+"/still_"+test_mode+str(test_option)
        self.checkdir(loc_path) # check if the directory for still logs exists else create it
        self.m_frw_tester.start_acquisition()
        #must has norebbot flag to keep serial port reading from rtos and linux else crash :(
        self.m_frw_tester.runTest(still=1,test_mode=test_mode,test_option=test_option)
        time.sleep(5)
        self.m_frw_tester.stop_acquisition()
        linux_rtos_logs = self.m_frw_tester.get_data()
        self.m_logger.write(loc_path+"/linux_ImageTest_log.txt",linux_rtos_logs[0])
        self.m_logger.write(loc_path+"/rtos_ImageTest_log.txt",linux_rtos_logs[1])
        self.copy_files(self.home_path + "/Desktop/test_capt", loc_path + "/test_capt")
        self.cleandir(self.home_path + "/Desktop/test_capt") #for each test delete the  generated files
        time.sleep(1.5)

    def cleanup(self):
        self.m_frw_tester.Rinit_camera()
        self.cleandir(self.home_path + "/Desktop/test_capt")
        time.sleep(1)
        clean_cmd = self.m_frw_tester.tcmdAgent.getCmd(clean=1) # delete all files in DCIM/100GOPRO
        self.m_frw_tester.Execute(clean_cmd)
        time.sleep(0.5)


    def flash_Test(self,arg_frw_type):

        loc_path = self.logs_path + "/flashTest"+arg_frw_type
        self.checkdir(loc_path) # this fuction check if the directory exists else create it
        self.m_frw_tester.start_acquisition()
        #self.m_frw_tester.flash_camera(arg_mode='make',arg_frw_type="spherical") #this reboots the platform
        self.m_frw_tester.turnOff_camera()
        self.m_frw_tester.flash_camera(arg_mode='arduino', arg_frw_type="spherical")
        time.sleep(5)
        self.m_frw_tester.stop_acquisition()
        linux_rtos_logs =self.m_frw_tester.get_data()
        self.m_logger.write(loc_path+"/linux_flashTest_log.txt",linux_rtos_logs[0])
        self.m_logger.write(loc_path+"/rtos_flashTest_log.txt",linux_rtos_logs[1])
        time.sleep(2)



#
# s= ScenarioMaker()
# s.cleandir(s.logs_path+"/still_5K_EAC_30_W_HEVC_IMX577None")




























