from frw_parser import frw_parser



"""

Maybe we add  timing functionalities to this class to limit tests with timeouts 

"""
class supervisor:

    def __init__(self):
        self.mfrw_parser = frw_parser()





    def isfirmwareBooted(self,arg_log_path):
        return_val = self.mfrw_parser.extract(arg_log_path,'compiled')
        if return_val == -1:
            raise Exception(' Problem with the Firmware , not a valid firmware !')
        else:
            print("Firmware booted correctly --------------> \n")
            print(return_val)



# supervisor = supervisor()
# supervisor.isfirmwareBooted('/home/saif/Logs/flashTestspherical/rtos_flashTest_log.txt')