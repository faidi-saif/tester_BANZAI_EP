from params import *

class tcmdGenerator:

    def __init__(self):
        self.commands =[]
        pass


    """ @mode must be like : 5K_EAC_30_W_HEVC_IMX577  
        @ option must be  =CALIB , PANO or None for PHOTO_18MP_30_W_IMX577    
    """
    def Still_genrate(self,arg_mode,arg_option=None):
        still_command_table = get_still_command_table()
        still_command_table[3] = "tcmd t frw test mode "+arg_mode
        if arg_option == "CALIB":
            tadditional = ["tcmd t frw cal raw 16",
                           "tcmd t frw cal bayer_width 4056",
                           "tcmd t frw test mode PHOTO_12MP_30_W_IMX577_DUAL_CAL"]
        elif arg_option == "PANO":
            tadditional = ["tcmd t frw test mode PHOTO_6MP_30_W_IMX577_PANO"]
        else :
            tadditional = ["tcmd t frw test mode PHOTO_18MP_30_W_IMX577"]

        still_command_table[9:9] = tadditional # 9 position of the the additional commands "
        return still_command_table


    """ @mode must be like : 5K_EAC_15_W_HEVC_IMX577  
        @ flare must be  =0,1,2
        @time : is the duration of the video t be tested     
    """

    def Video_generate(self,arg_mode,arg_flare,arg_time):

        param_dict['RUN_TIME'] = str(arg_time) #update variables and then generate command table
        video_command_table =get_video_command_table()
        video_command_table[0] = "tcmd t frw test mode " + arg_mode

        cmdflare = []
        if (arg_flare == 0):
            cmdflare.append("tcmd t frw stitch flare disable")
        else:
            cmdflare.append("tcmd t frw stitch flare enable")
            if(arg_flare == 2):
                cmdflare.append("echo 'Enabling identity flare corr with "+param_dict['FLARE_ID_FRONT_CORR']+"% of tiles budget for Front raw'")
                cmdflare.append("tcmd t frw stitch flare_id_cor enable "+param_dict['FLARE_ID_FRONT_CORR'])
            else:
                cmdflare.append("tcmd t frw stitch flare_id_cor disable")

        video_command_table[4:4] = cmdflare
        return video_command_table






    def adaptToUsb(self,arg_command_list):
        loc_commands =[]
        for command in arg_command_list:
            if "tcmd" in command :
                command = command.replace("tcmd ", "")
                command = "echo"+" '"+command+"'"
                command = command +" > /dev/ttyUSB1"
            loc_commands.append(command)
        return loc_commands



    def setup(self):
        return get_setup_command_table()


    def tear_down(self):
        return get_tear_down_command_table()

    def getCmd(self,clean = None,connect=None,display =None):
        if clean ==1:
            return "ssh root@" + param_dict['CAM_IP'] + " rm -rf /tmp/fuse_d/DCIM/100GOPRO/*"
        elif connect ==1:
            return "while ! timeout 0.5 ping " + param_dict['CAM_IP'] + " -c 1 ; do sleep 0.1; done"
        elif display ==1:
            return "ssh root@"+param_dict['CAM_IP']+" ls -l /tmp/fuse_d/DCIM/100GOPRO/"






    def generateCommands(self,still,test_mode,test_option=None,flare = 0 ,time = 4,noreboot = 1):

        list_commands = self.setup()
        if still ==1 :
            list_commands[len(list_commands):len(list_commands)] = self.Still_genrate(test_mode,test_option)
        else :
            list_commands[len(list_commands):len(list_commands)] =self.Video_generate(test_mode,flare,time)
        list_commands[len(list_commands):len(list_commands)] = self.tear_down()
        self.commands = self.adaptToUsb(list_commands) #
        return self.commands


    def __del__(self):
        pass







#
# tcmd =tcmdGenerator()
# tcmd.generateCommands(still=0,test_mode="5K_EAC_30_W_HEVC_IMX577", flare=0, time=4)
# for el in tcmd.commands :
#     print (el)





