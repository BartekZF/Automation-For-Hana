#!/usr/bin/env python3

import sys
import os
import re
import subprocess
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("-su", "--start_sap",
                    help="Start SAP", action="store_true")
parser.add_argument("-sd", "--stop_sap", help="Stop SAP", action="store_true")
parser.add_argument("-hu", "--start_hana",
                    help="Start HANA DB", action="store_true")
parser.add_argument("-hd", "--stop_hana",
                    help="Stop HANA DB", action="store_true")

args = parser.parse_args()


def find_sap_profile_hana():
    sap_profile_tmp = "grep -o 'pf=[^[:space:]]*' /usr/sap/sapservices | grep _HDB"
    sap_profile_tmp_hana = subprocess.check_output(
        sap_profile_tmp, shell=True, universal_newlines=True)
    sap_profile_hana = str(sap_profile_tmp_hana).split()
    # print(sap_profile_hana)
    return sap_profile_hana


def read_hana_sid():
    sap_profile_hana_tmp = str(find_sap_profile_hana())
    hana_sid = sap_profile_hana_tmp.split('/')[-1][0:3]
    # print(hana_sid)
    return hana_sid


def read_hana_instance_id():
    hana_instance_id_tmp = str(find_sap_profile_hana())
    hana_instance_sid_split = hana_instance_id_tmp.split('/')[-1]
    hana_instance_sid = hana_instance_sid_split.split('_')[1][3:5]
    # print(hana_instance_sid)
    return hana_instance_sid


if args.start_hana:
    hana_instance_start = os.system("/usr/sap/hostctrl/exe/sapcontrol -nr " +
                                    read_hana_instance_id() + " -function StartService " + read_hana_sid())
    hana_instance_wait = os.system("/usr/sap/hostctrl/exe/sapcontrol -nr " +
                                   read_hana_instance_id() + " -function WaitforServiceStarted 10 2")
    hana_instance_start = os.system(
        "/usr/sap/hostctrl/exe/sapcontrol -nr " + read_hana_instance_id() + " -function Start")
    hana_instance_list = os.system("/usr/sap/hostctrl/exe/sapcontrol -nr " +
                                   read_hana_instance_id() + " -function GetSystemInstanceList")
    time.sleep(240)
    print(hana_instance_start)
    print(hana_instance_wait)
    print(hana_instance_start)
    print(hana_instance_list)

if args.stop_hana:
    hana_instance_stop = os.system(
        "/usr/sap/hostctrl/exe/sapcontrol -nr " + read_hana_instance_id() + " -function StopWait 600 2")
    hana_instance_list = os.system("/usr/sap/hostctrl/exe/sapcontrol -nr " +
                                   read_hana_instance_id() + " -function GetSystemInstanceList")
    print(hana_instance_list)
