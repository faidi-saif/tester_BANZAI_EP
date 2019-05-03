from ScenarioMaker import ScenarioMaker
import time


"""
    @ /******************************************************************************************/
    @ /*                              CleanUp-Reset-Flash                                       */
    @ /*                                                                                        */
    @ /******************************************************************************************/

"""
#--------------------------------------------- Instantiate ScenarioMaker -----------------------------------------------
mScenarioMaker = ScenarioMaker()
#-------------------------------------------------- cleanup ------------------------------------------------------------
#mScenarioMaker.cleanup()
#-------------------------------------------------- flash-test  --------------------------------------------------------
#mScenarioMaker.flash_Test(arg_frw_type="spherical")

#--------------------------------------------------- reset-test--------------------------------------------------------
print ("\ntest1   ==>  Reset Camera ------------------------------------->  \n")
mScenarioMaker.Reset_Test()


"""
    @ /******************************************************************************************/
    @ /*                                    VIDEOS                                              */
    @ /*                                                                                        */
    @ /******************************************************************************************/

"""

print("\ntest2 ==> test video -------------------------------------> *5K_EAC_30_W_HEVC_IMX577  *time =2  *flare =1 \n")
mScenarioMaker.Test_video(test_mode="5K_EAC_30_W_HEVC_IMX577", flare=1, arg_time=2)


mScenarioMaker.m_frw_tester.reset_camera()

#
# print("\nTest3 ==> test video -------------------------------------> *5K_EAC_24_W_HEVC_IMX577  *time =2  *flare =1 \n")
# mScenarioMaker.Test_video(test_mode="5K_EAC_24_W_HEVC_IMX577", flare=1, arg_time=2)
#
#
#
# mScenarioMaker.m_frw_tester.reset_camera()
#
#
#
# """
#     @ /******************************************************************************************/
#     @ /*                                    IMAGES                                              */
#     @ /*                                                                                        */
#     @ /******************************************************************************************/
#
# """
#
#
# print("\nTest 4 ==> test image -------------------------------------> *5K_EAC_30_W_HEVC_IMX577*  *No CALIB*  *No PANO* \n ")
# mScenarioMaker.Test_image(test_mode="5K_EAC_30_W_HEVC_IMX577")
#
#
# mScenarioMaker.m_frw_tester.reset_camera()
#
#
#
# print("\nTest 5 ==> test image ------------------------------------->*5K_EAC_30_W_HEVC_IMX577*  *No CALIB*  * PANO* \n ")
# mScenarioMaker.Test_image(test_mode="5K_EAC_30_W_HEVC_IMX577",test_option="PANO")
#


#mScenarioMaker.m_frw_tester.Rinit_camera()
#mScenarioMaker.m_frw_tester.reset_camera()
# mScenarioMaker.m_frw_tester.turnOff_camera()
# time.sleep(6)
# mScenarioMaker.m_frw_tester.turnOn_camera()
# time.sleep(4)
# mScenarioMaker.m_frw_tester.reset_camera()


