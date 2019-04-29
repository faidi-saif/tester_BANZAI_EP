from ScenarioMaker import ScenarioMaker
import time





"""
    @ /******************************************************************************************/
    @ /*                             Init - CleanUp - RESET                                     */
    @ /*                                                                                        */
    @ /******************************************************************************************/

"""


mScenarioMaker = ScenarioMaker()
mScenarioMaker.cleanup() # get the reinit back !
print ("\nTest1   ==>  Camera Reset --------------->  \n")
mScenarioMaker.Reset_Test()
time.sleep(2)


"""
    @ /******************************************************************************************/
    @ /*                                    VIDEOS                                              */
    @ /*                                                                                        */
    @ /******************************************************************************************/

"""

# print("\nTest2 ==> test video -------------> *5K_EAC_30_W_HEVC_IMX577  *time =2  *flare =1 \n")
# mScenarioMaker.Test_video(test_mode="5K_EAC_30_W_HEVC_IMX577", flare=1, arg_time=4)
#
# time.sleep(3)
# mScenarioMaker.reset()
# time.sleep(3)
#
# print("\nTest3 ==> test video -------------> *5K_EAC_24_W_HEVC_IMX577  *time =2  *flare =1 \n")
# mScenarioMaker.Test_video(test_mode="5K_EAC_24_W_HEVC_IMX577", flare=1, arg_time=4)
#
#
# time.sleep(3)
# mScenarioMaker.reset()
# time.sleep(3)
# """
#     @ /******************************************************************************************/
#     @ /*                                    IMAGES                                              */
#     @ /*                                                                                        */
#     @ /******************************************************************************************/
#
# """
#
#
# print("\nTest 4 ==> test image -----------> *5K_EAC_30_W_HEVC_IMX577*  *No CALIB*  *No PANO* \n ")
# mScenarioMaker.Test_image(test_mode="5K_EAC_30_W_HEVC_IMX577")
#
# time.sleep(3)
# mScenarioMaker.reset()
# time.sleep(3)
#
#
# print("\nTest 5 ==> test image -----------> *5K_EAC_30_W_HEVC_IMX577*  *No CALIB*  * PANO* \n ")
# mScenarioMaker.Test_image(test_mode="5K_EAC_30_W_HEVC_IMX577",test_option="PANO")
#
# time.sleep(3)
# #
#
#



"""
@ test firmware reset
"""


"""
@step1 : python waf configure
"""
# c_o_e = get_exitcode_stdout_stderr("python waf configure")
# if c_o_e[0] != 0:
#   eror_mess = "exception while running 'python waf configure' \n {}".format(c_o_e[2])
#   raise Exception(eror_mess)
# else:
#   print(c_o_e[1])
#   print("\n ====> configure succeeded\n")

"""
@step2 : make libs
"""
# c_o_e = get_exitcode_stdout_stderr("make libs")
# if c_o_e[0] != 0:
#   eror_mess = "exception while running 'make libs' \n {}".format(c_o_e[2])
#   raise Exception(eror_mess)
# else:
#   print(c_o_e[1])
#   print("\n ====> make libs succeeded\n")

"""
@step3 : make sdk
"""

# c_o_e = get_exitcode_stdout_stderr("make sdk")
# if c_o_e[0] != 0:
#   eror_mess = "exception while running 'make sdk' \n {}".format(c_o_e[2])
#   raise Exception(eror_mess)
# else:
#   print(c_o_e[1])
#   print("\n ====> make sdk succeeded\n")

"""
@step4 : make fw
"""

# c_o_e = get_exitcode_stdout_stderr("make fw")
# if c_o_e[0] != 0:
#   eror_mess = "exception while running 'make fw' \n {}".format(c_o_e[2])
#   raise Exception(eror_mess)
# else:
#   print(c_o_e[1])
#   print("\n ====> make fw succeeded\n")

"""
@step5 :make fw-flash
"""

# c_o_e = get_exitcode_stdout_stderr("make fw-flash")
# if c_o_e[0] != 0:
#   eror_mess = "exception while running 'make fw-flash' \n {}".format(c_o_e[2])
#   raise Exception(eror_mess)
# else:
#   print(c_o_e[1])
#   print(" \n ====> flash the camera is done succeeded\n")


"""
@step6 :check if binary for spherical exists
"""
# b_path = os.environ['HOME']+"/BANZAI_EP/waf_build/spherical/build/eaglepeak/sd_fwupdate/DATA.bin"
# check_file_exist(b_path,"make sure VARIANT is set to spherical , No file found")





#m_frw_tester.ReadFromRtos()
# arg_cmd="./spherical_test.sh -getresult -record -time 5"
# m_frw_tester.Execute_Test(arg_cmd)
#m_frw_tester.flash_camera()
#m_frw_tester.reset_camera()
#m_frw_tester.reset_camera()
#print(m_frw_tester.Test_case())
#m_frw_tester.Test_case()


