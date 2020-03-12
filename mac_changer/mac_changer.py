#!/usr/bin/env python

import subprocess


subprocess.call("ifconfig wlp7s0 down", shell=True)
subprocess.call("ifconfig wlp7s0 hw ether BC:AE:C5:BE:8B:B7", shell=True)
subprocess.call("ifconfig wlp7s0 up", shell=True)
