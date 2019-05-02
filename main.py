from ScenarioMaker import ScenarioMaker
import time



"""
    @ /******************************************************************************************/
    @ /*                              Init- flash - powerOn                                             */
    @ /*                                                                                        */
    @ /******************************************************************************************/

"""

mScenarioMaker = ScenarioMaker()
mScenarioMaker.flash_Test(arg_frw_type="spherical")

"""
    @ /******************************************************************************************/
    @ /* reset all the instance of serial ports since flashing the firmware kills this instances*/
    @ /*                                                                                        */
    @ /******************************************************************************************/

"""
#mScenarioMaker.m_frw_tester.Rinit_camera()
#
# mScenarioMaker.reset()
# mScenarioMaker.m_frw_tester.turnOff_camera()
# time.sleep(6)
# mScenarioMaker.m_frw_tester.turnOn_camera()
# time.sleep(4)
# mScenarioMaker.reset()

"""
    @ /******************************************************************************************/
    @ /*                              CleanUp - RESET                                           */
    @ /*                                                                                        */
    @ /******************************************************************************************/

"""


# mScenarioMaker = ScenarioMaker()
# mScenarioMaker.cleanup() # get the reinit back !
# print ("\nTest1   ==>  Camera Reset --------------->  \n")
# mScenarioMaker.Reset_Test()
# time.sleep(2)

#
# """
#     @ /******************************************************************************************/
#     @ /*                                    VIDEOS                                              */
#     @ /*                                                                                        */
#     @ /******************************************************************************************/
#
# """
#
# print("\nTest2 ==> test video -------------> *5K_EAC_30_W_HEVC_IMX577  *time =2  *flare =1 \n")
# mScenarioMaker.Test_video(test_mode="5K_EAC_30_W_HEVC_IMX577", flare=1, arg_time=2)
#
# time.sleep(3)
# mScenarioMaker.reset()
# time.sleep(3)
#
# print("\nTest3 ==> test video -------------> *5K_EAC_24_W_HEVC_IMX577  *time =2  *flare =1 \n")
# mScenarioMaker.Test_video(test_mode="5K_EAC_24_W_HEVC_IMX577", flare=1, arg_time=2)
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
#



