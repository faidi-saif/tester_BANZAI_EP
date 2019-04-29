import os
##import sys
import shlex
from subprocess import *
from serializer_ForArduino import*
from serializer_Reader import*
from tcmdGenerator import *



class frw_tester :


    def __init__(self):

        self.serializer_ForArduino = serializer_ForArduino('/dev/ARDUINO',9600)
        self.serializer_ForRTOS = serializer_Reader('/dev/RTOS',115200,"RTOS")
        self.serializer_ForLinux = serializer_Reader('/dev/LINUX', 115200,"LINUX")
        self.tcmdAgent =tcmdGenerator()
        self.abspath = os.environ['HOME'] #abstract path = ~  , /var/lib/jenkins or /home/saif
        self.LINUX_log = ""
        self.RTOS_log = ""
        # os.environ['CAM_IP']='192.168.0.202'
        # os.environ['TARGET_DIR']='~/Desktop/test_capt'



    """
        @ /******************************************************************************************/
        @ /*  to run this script correctly you must have BANZAI_EP in the "~/" directory            */
        @ /*                                 LOW LEVEL APIS                                         */
        @ /*                                                                                        */
        @ /******************************************************************************************/

    """



    def process_cmd(self,cmd): #takes a shell command and execute it
        args = shlex.split(cmd)
        proc = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        exitcode = proc.returncode
        return exitcode, out, err



    def Execute(self,arg_cmd):
        self.goto_path("/BANZAI_EP/framework/test/test_cases")
        ret = os.system(arg_cmd)
        if ret != 0:
            linux_rtos_logs = self.get_data()
            print("linux ------------------------------> : \n"+linux_rtos_logs[0])
            print("rtos  ------------------------------> : \n: \n" + linux_rtos_logs[1])
            raise Exception(" command : " + arg_cmd+" failed to execute")

        #print("command to be executed : ",arg_cmd)
        # c_o_e= self.process_cmd(arg_cmd)
        # if c_o_e[0] != 0:
        #     eror_mess = "can't process",str(arg_cmd)," \n {}".format(c_o_e[2])
        #     raise Exception(eror_mess)
        # else:
        #     print(c_o_e[1])




    def goto_path(self,arg_path):
        # abstpath is our home directory
        try:
            l_path = self.abspath +arg_path #/BANZAI_EP"
            # banzai_root = os.path.join("/",*banzai_root.split("/"),"BANZAI_EP")
            os.chdir(l_path)
            # print(os.environ["HOME"])
            #print(">", os.getcwd())
        except:
            print("Unexcepted error , please make sure",arg_path ,"directory is in your", '"', self.abspath,
                  '"', "directory")




    def __del__(self):
        del self.serializer_ForRTOS
        pass






    """
    @ /******************************************************************************************/
    @ /*                                                                                        */
    @ /*                                 HIGH LEVEL APIS                                        */                    
    @ /*                                                                                        */
    @ /******************************************************************************************/
    
    """


    def check_file_exist(self,arg_path, arg_error_message):
        exists = os.path.isfile(arg_path)
        if exists:
            print("path => ", arg_path, "exists Ok !")
        else:
            raise Exception(arg_error_message)


    #default test ===> ./spherical_test.sh -getresult -record -time 6 -fps 30
    # def Test_case(self,still=None,time=6,keep_previous_dump=None,noflare=None,noreboot=None,fps=30):
    #     shell_cmd = "./spherical_test.sh -getresult -record"
    #     # in options make sure there is spaces at the beining and at the end
    #     options = {" -keep_previous_dump": keep_previous_dump, " -noflare": noflare,
    #                " -noreboot ": noreboot}
    #
    #     def create_options():
    #         additional_options=""
    #         for opt_name, opt_value in options.items():
    #             if opt_value != None:
    #                 additional_options = additional_options + opt_name
    #                 # print(opt_name)
    #         return additional_options
    #     if still == None:
    #     # video
    #         shell_cmd =shell_cmd+" -time "+str(time)+" -fps "+str(fps)+create_options()
    #     else:
    #         # Image
    #         shell_cmd = shell_cmd+" -still" + create_options()
    #     self.Execute(shell_cmd)
    """
    @test_mode is a test flag must be : for example: 
    5K_EAC_15_W_HEVC_IMX577
    5K_EAC_30_W_HEVC_IMX577
    5K_EAC_25_W_HEVC_${LRV}IMX577 
    
    @option must be  : CALIB , PANO fro still
    
    """
    def runTest(self,still,test_mode,test_option = None,flare =0,time= 4,noreboot=1,):
        commands = self.tcmdAgent.generateCommands(still,test_mode,test_option,flare,time)
        for shell_cmd in commands :
            #print(shell_cmd)
            self.Execute(shell_cmd)









    def reset_camera(self):
        self.serializer_ForArduino.reset()


    def flash_camera(self):
        self.serializer_ForArduino.fw_flash()


    def power_camera(self):
        self.serializer_ForArduino.PowerOn()


    def turnOff_camera(self):
        self.serializer_ForArduino.PowerOff()


    def Rinit_camera(self):
        self.serializer_ForArduino.reinitialise()


    def start_acquisition(self):
        self.serializer_ForRTOS.start_acquisition()
        self.serializer_ForLinux.start_acquisition()


    def stop_acquisition(self):
        self.serializer_ForRTOS.stop_acquisition()
        self.serializer_ForLinux.stop_acquisition()

    def get_data(self):
        self.LINUX_log = self.serializer_ForLinux.getData()
        self.RTOS_log = self.serializer_ForRTOS.getData()
        m_data=[self.LINUX_log,self.RTOS_log]
        return m_data







#
# tester = frw_tester()
# tester.reset_camera()
# os.system("echo 't appc status disable' > /dev/ttyUSB1")
# tester.Execute("echo 't appc status disable' > /dev/ttyUSB1")







