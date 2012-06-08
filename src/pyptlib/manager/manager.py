import os
import subprocess

class Manager:
  def __init__(self):
    os.environ['TOR_PT_STATE_LOCATION']='/'
    os.environ['TOR_PT_MANAGED_TRANSPORT_VER']='1'

  def launch(self, str):
    p=subprocess.Popen(str, stdout=subprocess.PIPE)
    f=p.stdout
    b=f.read()
    print(b)
    