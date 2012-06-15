import os
import sys
import subprocess

class Manager:
  def __init__(self):
    os.environ['TOR_PT_STATE_LOCATION']='/'
    os.environ['TOR_PT_MANAGED_TRANSPORT_VER']='1'

  def launch(self, path):
    p=subprocess.Popen(path, stdout=subprocess.PIPE)
    for b in p.stdout:
      print('b: '+str(b))
      sys.stdout.flush()
    print('Done!')
