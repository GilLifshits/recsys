import os
import sys

os.system("nohup bash -c '" + sys.executable + " train.py --size 192 >result.txt" + "' &")