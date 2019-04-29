
#
#@ this script contains the encoded value
#@sent on usart to control the camera
#@ using arduino
#@
#
RE_INIT = str.encode("Z")

PRESS_EP_RST = str.encode("P0")
RELEASE_EP_RST = str.encode("R0")
VOLT_RST = str.encode("V0")

PRESS_JTAG_RST = str.encode("P1")
RELEASE_JTAG_RST = str.encode("R1")
VOLT_JTAG =str.encode("V1")

PRESS_SHUTT = str.encode("P2")
RELEASE_SHUTT = str.encode("R2")
VOLT_SHUTT = str.encode("V2")

PRESS_POW = str.encode("P3")
RELEASE_POW = str.encode("R3")
VOLT_POWER = str.encode("V3")


#
#@ Test setup
#@
#



# RING_USE_HIGH_RES ="enable"
# FLARE_FAKE_TIME ='0'
# FLARE_ID_FRONT_CORR='50'
# FLARE_FAKE='disable'
# CAM_IP="192.168.0.202"
# TARGET_DIR='~/Desktop/test_capt'
# LRV=""
# STUB='disable'
# VERBOSE='off'
# RUN_TIME='5'

param_dict ={'RING_USE_HIGH_RES':"enable",
             'FLARE_FAKE_TIME':'0',
             'FLARE_ID_FRONT_CORR':'50',
             'FLARE_FAKE':'disable',
             'CAM_IP':'192.168.0.202',
             'TARGET_DIR':'~/Desktop/test_capt',
             'LRV':"",
             'STUB':'disable',
             'VERBOSE':'off',
             'RUN_TIME':'5'}
#
# "echo 'Setting flare_fake_dsp_sleep to $FLARE_FAKE (sleep=$FLARE_FAKE_TIME)'",
# "tcmd t frw stitch flare_fake_dsp_sleep $FLARE_FAKE $FLARE_FAKE_TIME",
# "echo 'Setting ring_high_res to $RING_USE_HIGH_RES'",
# "tcmd t frw stitch ring_high_res $RING_USE_HIGH_RES"
def get_setup_command_table():
    setup_command_table = ["tcmd t appc status disable",
                   "sleep 3",
                   "tcmd t frw cpu_boost enable",
                   "tcmd t hal act9150 reg 0x32 0x2C",
                   "tcmd t hal act9150 reg 0x33 0x2C",
                   "tcmd t hal mxm_coreclk_ctrl set_freq 660000000",
                   "tcmd t dbg off",
                   "sleep 0.5",
                   "tcmd t frw test disp_id 0",
                   "tcmd t frw test open",
                   "tcmd t frw audproc enable_awe 0",
                   "echo 'Setting flare_fake_dsp_sleep to "+param_dict['FLARE_FAKE']+" (sleep="+param_dict['FLARE_FAKE_TIME']+")'",
                   "tcmd t frw stitch flare_fake_dsp_sleep "+param_dict['FLARE_FAKE']+" "+param_dict['FLARE_FAKE_TIME'],
                   "echo 'Setting ring_high_res to "+param_dict['RING_USE_HIGH_RES']+"'",
                   "tcmd t frw stitch ring_high_res "+param_dict['RING_USE_HIGH_RES']
                    ]
    return setup_command_table

cmode_still = "tcmd t frw test mode 5K_EAC_30_W_HEVC_IMX577"
#must treeat the CALIB and the PANO cases , and 5k_EAC_30
def get_still_command_table():
     still_command_table= [ "echo 'Launch Still Capture'",
                               "tcmd t dbg off",
                               "tcmd t frw stitch stub enable",
                               cmode_still,
                               "sleep 0.1",
                               "tcmd t frw test graph still_spherical",
                               "tcmd t frw test liveview",
                               "sleep 1.5",
                               "tcmd t dbg "+param_dict['VERBOSE'],
                               "sleep 0.5",
                               "tcmd t frw stitch stub disable",
                               "tcmd t frw test still",
                               "sleep 4",
                               "tcmd t frw test stop_still",
                               "sleep 2",
                               "tcmd t dbg off",
                               "tcmd t frw test mode 5K_EAC_30_W_HEVC_IMX577",
                               "tcmd t frw stitch stub enable",
                               "tcmd t frw test liveview",
                               "echo 'Still Done'",
                           ]
     return still_command_table


cmode_video = "tcmd t frw test mode 5K_EAC_30_W_HEVC_${LRV}IMX577"
def get_video_command_table():
    video_command_table= [     cmode_video,
                               "sleep 0.5",
                               "tcmd t frw test graph video_spherical",
                               "tcmd t frw stitch stub "+param_dict['STUB'],
                               "sleep 1",
                               "tcmd t frw test liveview",
                               "sleep 0.5",
                               "tcmd t dbg "+param_dict['VERBOSE'],
                               "sleep 0.5",
                               "sleep 10",
                               "sleep 0.5",
                               "echo 'Launch Record for "+param_dict['RUN_TIME']+" s'",
                               "tcmd t frw test start_video",
                               "sleep 0.1",
                               "sleep "+param_dict['RUN_TIME'],
                               "echo 'Stop Record'",
                               "tcmd t frw test stop_video",
                               "tcmd t dbg "+param_dict['VERBOSE'],
                                ]
    return video_command_table

def get_tear_down_command_table():
    tear_down_command_table= [ "while ! timeout 0.5 ping "+param_dict['CAM_IP']+" -c 1 ; do sleep 0.1; done",
                               "ssh root@"+param_dict['CAM_IP']+" ls /tmp/fuse_d/DCIM/100GOPRO",
                               "tcmd t dbg off",
                               "mkdir -p "+param_dict['TARGET_DIR'],
                               "ssh root@"+param_dict['CAM_IP']+" ls -l /tmp/fuse_d/DCIM/100GOPRO/",
                               "./tear_down.sh",
                               "ssh root@" + param_dict['CAM_IP'] + " rm -rf /tmp/fuse_d/DCIM/100GOPRO/*"
                             ]
    return tear_down_command_table

# def get_tear_down_command_table():
#     tear_down_command_table= [ "while ! timeout 0.5 ping "+param_dict['CAM_IP']+" -c 1 ; do sleep 0.1; done",
#                                "ssh root@"+param_dict['CAM_IP']+" ls /tmp/fuse_d/DCIM/100GOPRO",
#                                "tcmd t dbg off",
#                                "mkdir -p "+param_dict['TARGET_DIR'],
#                                "ssh root@"+param_dict['CAM_IP']+" ls -l /tmp/fuse_d/DCIM/100GOPRO/",
#                                "files=$(ssh root@"+param_dict['CAM_IP']+" ls /tmp/fuse_d/DCIM/100GOPRO/)",
#                                "for file in $files ;  do wget  "+param_dict['CAM_IP']+":8042/DCIM/100GOPRO/$file -O "+param_dict['TARGET_DIR']+"/$file ;done",
#                                "ssh root@" + param_dict['CAM_IP'] + " rm -rf /tmp/fuse_d/DCIM/100GOPRO/*"
#                              ]
#
#     return tear_down_command_table

