from frw_tester import *
from logger import *
import os
import shutil
from supervisor import supervisor
import timeout_decorator



class ScenarioMaker:

    # ------------------------------------------------ constructor  ----------------------------------------------------------
    def __init__(self):
        # ------------------------------------------------ instantiation ------------------------------------------------------
        self.m_frw_tester = frw_tester()
        self.m_logger = logger()
        self.supervisor = supervisor()
        # ------------------------------------------- goto ~/BANZAI_EP ---------------------------------------------------------
        self.m_frw_tester.goto_path("/BANZAI_EP")
        self.home_path =self. m_frw_tester.abspath
        # ---------------------------------------- create the root path for Logs -----------------------------------------------
        self.logs_path = os.environ["HOME"] + "/Logs"
        # ------------------------------check if the logs directory exists else create it --------------------------------------
        self.checkdir(self.logs_path)
        # ------------------------------clean all logs from previous test ------------------------------------------------------
        self.cleandir(self.logs_path)


    # def reset(self):
    #     self.m_frw_tester.__del__()
    #     self.m_frw_tester.__init__()

    # ----------------------------------- check if a given directory exists else create it ------------------------------------

    def checkdir(self,arg_path):
        if os.path.isdir(arg_path):
            pass
        else:
            os.mkdir(arg_path)


    # ---------------------------------------- remove all files in a given path -----------------------------------------------

    def cleandir(self,arg_path):
        for the_file in os.listdir(arg_path):
            file_path = os.path.join(arg_path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

    # ------------------------------------------------ destructor --------------------------------------------------------------
    def __del__(self):
        self.m_frw_tester.__del__()

    # -------------------------------------------copy files in a given path ( remove it to logger class )-----------------------
    def copy_files(self,from_path, to_path):
        if os.path.exists(to_path):
            #self.cleandir(to_path)
            shutil.rmtree(to_path)
        shutil.copytree(from_path, to_path)



    # ------------------------------------------------ function called before test starts---------------------------------------
    @timeout_decorator.timeout(180) # 3min of delay
    def cleanup(self):
        #-------start with a valid firmware : reflash the platform with a valid firmware using arduino ( ref-firmware)-----------------------------------------> call it when driver for power cut will be developed
        #self.m_frw_tester.flash_camera(arg_mode='arduino', arg_frw_type="spherical")
        #time.sleep(10)
        # ------------------------------------------------ reset-camera --------------------------------------------------------
        self.m_frw_tester.reset_camera()
        # ------------------------------------------------ time to reset --------------------------------------------------------
        time.sleep(2)
        # -------------------------------------clean test_capt (if previous test crashed ) --------------------------------------
        self.cleandir(self.home_path + "/Desktop/test_capt")
        time.sleep(1)
        # -------------------------------------remove all files in DCIM/100GOPRO (if previous test crashed )  --------------------
        clean_cmd = self.m_frw_tester.tcmdAgent.getCmd(clean=1)
        self.m_frw_tester.Execute(clean_cmd)
        time.sleep(0.5)


    @timeout_decorator.timeout(180)# 3min of delay
    def Reset_Test(self):
        # --------------------------------- create folder for reset logs ----------------------------------------------------------
        loc_path =self.logs_path+"/ResetTest"
        self.checkdir(loc_path)
        # ----------------------------------------- start logs (rtos,linux) acquisition  ------------------------------------------
        self.m_frw_tester.start_acquisition()
        # ----------------------------------------- reset camera  -----------------------------------------------------------------
        self.m_frw_tester.reset_camera()
        # ----------------------------------------- wait for reset  ---------------------------------------------------------------
        time.sleep(5)
        # ----------------------------------------- stop logs (rtos,linux) acquisition  ------------------------------------------
        self.m_frw_tester.stop_acquisition()
        # ----------------------------------------- get logs (rtos,linux) ---------------------------------------------------------
        linux_rtos_logs =self.m_frw_tester.get_data()
        self.m_logger.write(loc_path+"/linux_ResetTest_log.txt",linux_rtos_logs[0])
        self.m_logger.write(loc_path+"/rtos_ResetTest_log.txt",linux_rtos_logs[1])


    @timeout_decorator.timeout(300)# 5min of delay
    def Test_video(self,test_mode,flare=1,arg_time=4):
        # --------------------------create folder for video logs based on test_mode -----------------------------------------------
        loc_path = self.logs_path + "/test_video_"+test_mode
        self.checkdir(loc_path)
        # ----------------------------------------- start logs (rtos,linux) acquisition  ------------------------------------------
        self.m_frw_tester.start_acquisition()
        # ----------------------------------------- still = 0 for video test  -----------------------------------------------------
        self.m_frw_tester.runTest(still=0,test_mode="5K_EAC_30_W_HEVC_IMX577", flare=flare, time=arg_time)
        time.sleep(5)
        # ----------------------------------------- stop logs (rtos,linux) acquisition  ------------------------------------------
        self.m_frw_tester.stop_acquisition()
        # ----------------------------------------- get logs (rtos,linux) ---------------------------------------------------------
        linux_rtos_logs = self.m_frw_tester.get_data()
        # ----------------------------------------- write logs (rtos,linux) in logs path--------------------------------------------
        self.m_logger.write(loc_path + "/linux_"+test_mode+"video_log.txt", linux_rtos_logs[0])
        self.m_logger.write(loc_path + "/rtos_"+test_mode+"video_log.txt", linux_rtos_logs[1])
        # ---------------------------------------  copy files from test_capt to the log directory-----------------------------------
        self.copy_files(self.home_path+"/Desktop/test_capt",loc_path+"/test_capt")
        # --------------------- clean test_capt folder after each test to keep the logs clean for the following test----------------
        self.cleandir(self.home_path + "/Desktop/test_capt")
        time.sleep(1.5)


    @timeout_decorator.timeout(300)# 5min of delay
    def Test_image(self,test_mode="5K_EAC_30_W_HEVC_IMX577",test_option=None):
        # --------------------------create folder for still logs based on test mode and option ( 'PANO , CALIB ' )-----------------
        loc_path =self.logs_path+"/still_"+test_mode+str(test_option)
        # ------------------------------check if the logs directory exists else create it -----------------------------------------
        self.checkdir(loc_path)
        # ----------------------------------------- start logs (rtos,linux) acquisition  ------------------------------------------
        self.m_frw_tester.start_acquisition()
        # ----------------------------------------- still = 1 for image test  -----------------------------------------------------
        self.m_frw_tester.runTest(still=1,test_mode=test_mode,test_option=test_option)
        time.sleep(5)
        # ----------------------------------------- stop logs (rtos,linux) acquisition  ------------------------------------------
        self.m_frw_tester.stop_acquisition()
        # ----------------------------------------- get logs (rtos,linux) ---------------------------------------------------------
        linux_rtos_logs = self.m_frw_tester.get_data()
        # ----------------------------------------- write logs (rtos,linux) in logs path--------------------------------------------
        self.m_logger.write(loc_path+"/linux_ImageTest_log.txt",linux_rtos_logs[0])
        self.m_logger.write(loc_path+"/rtos_ImageTest_log.txt",linux_rtos_logs[1])
        # ---------------------------------------  copy files from test_capt to the log directory-----------------------------------
        self.copy_files(self.home_path + "/Desktop/test_capt", loc_path + "/test_capt")
        # --------------------- clean test_capt folder after each test to keep the logs clean for the following test----------------
        self.cleandir(self.home_path + "/Desktop/test_capt") #for each test delete the  generated files
        time.sleep(1.5)


    @timeout_decorator.timeout(360)# 6min of delay
    def flash_Test(self,arg_frw_type):
        # --------------------------create folder for flash logs based on the type of flashing ( 'spherical ....' )---------------
        loc_path = self.logs_path + "/flashTest"+arg_frw_type
        # ------------------------------check if the logs directory exists else create it -----------------------------------------
        self.checkdir(loc_path)
        # ----------------------------------------- start logs (rtos,linux) acquisition  ------------------------------------------
        self.m_frw_tester.start_acquisition()
        # -------------------------------------------flash camera with new firmware  ------------------------------------------------
        self.m_frw_tester.flash_camera(arg_mode='make',arg_frw_type=arg_frw_type) #this reboots the platform
        # -------------------------------------------time for flashing -----------------------------------------------------------
        time.sleep(10)
        # ----------------------------------------- get list of commands to check if the rtos boots -------------------------------
        check_boot_cmd = self.m_frw_tester.tcmdAgent.getCmd(rtos_version_test=1)
        # ----------------------------------------- run commands for boot test ----------------------------------------------------
        self.m_frw_tester.runScenario(check_boot_cmd)
        time.sleep(2)
        # ----------------------------------------- stop logs (rtos,linux) acquisition  ------------------------------------------
        self.m_frw_tester.stop_acquisition()
        # ----------------------------------------- get logs (rtos,linux) ---------------------------------------------------------
        linux_rtos_logs =self.m_frw_tester.get_data()
        # ----------------------------------------- write logs (rtos,linux) in logs path--------------------------------------------
        rtos_log_path = loc_path+"/rtos_flashTest_log.txt"
        self.m_logger.write(loc_path+"/linux_flashTest_log.txt",linux_rtos_logs[0]) #write data
        self.m_logger.write(rtos_log_path,linux_rtos_logs[1])
        # ----------------------------------------- check if the firmware is correctly booted----------------------------------------
        self.supervisor.isfirmwareBooted(rtos_log_path)




#
# s= ScenarioMaker()
# s.cleandir(s.logs_path+"/still_5K_EAC_30_W_HEVC_IMX577None")




























