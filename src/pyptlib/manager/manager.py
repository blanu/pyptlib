import os

class Manager:
  def __init__(self):
    os.environ['TOR_PT_STATE_LOCATION']='/'
    os.environ['TOR_PT_MANAGED_TRANSPORT_VER']='1'
    
    