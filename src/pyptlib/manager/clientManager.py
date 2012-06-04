import os

from manager import manager

class ClientManager(Manager):
  def __init__(self):
    Manager.__init__(self)
  
    os.environ['TOR_PT_CLIENT_TRANSPORTS']='dummy'
    
    