import os

from config import Config

"""
Configuration for a Pluggable Transport client.
"""

__docformat__ = 'restructuredtext'


class ClientConfig(Config):
  clientTransports=[] # TOR_PT_CLIENT_TRANSPORTS
  
  def __init__(self): # throws EnvError
    Config.__init__(self)
    
    clientTransports=self.get('TOR_PT_CLIENT_TRANSPORTS').split(',')
    
  # Returns a list of strings representing the client transports reported by Tor. If present, '*' is stripped from this list and used to set allTransportsEnabled to True.
  def getClientTransports(self):
    return clientTransports

  # Write a message to stdout specifying a supported transport
  # Takes: str, int, (str, int), [str], [str]
  def writeMethod(self, name, socksVersion, address, args, optArgs): # CMETHOD
    s='CMETHOD '+str(name)+' socks'+str(socksVersion)+' '+str(address[0])+':'+str(address[1])
    if args and len(args)>0:
      s=s+' ARGS='+args.join(',')
    if optArgs and len(optArgs)>0:
      s=s+' OPT-ARGS='+args.join(',')
    print(s) 
   
  # Write a message to stdout specifying that an error occurred setting up the specified method
  # Takes: str, str
  def writeMethodError(self, name, message): # CMETHOD-ERROR
    print('CMETHOD-ERROR '+str(name)+' '+str(message))
    
  # Write a message to stdout specifying that the list of supported transports has ended
  def writeMethodEnd(self): # CMETHODS DONE
    print('CMETHODS DONE')
