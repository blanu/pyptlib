import os

from config import Config

"""
Configuration for a Pluggable Transport server.
"""

__docformat__ = 'restructuredtext'

class ServerConfig(Config):
  extendedServerPort=None # TOR_PT_EXTENDED_SERVER_PORT
  ORPort=None             # TOR_PT_ORPORT
  serverBindAddr={}       # TOR_PT_SERVER_BINADDR
  serverTransports=[]     # TOR_PT_SERVER_TRANSPORTS
  
  def __init__(self): # throws EnvError
    Config.__init__(self)
    
    extendedServerPort=get('TOR_PT_EXTENDED_SERVER_PORT')
    ORPort=get('TOR_PT_ORPORT')
    
    binds=get('TOR_PT_SERVER_BINADDR').split(',')
    for bind in binds:
      key,value=bind.split(',')
      serverBindAddr[key]=value
    
    serverTransports=get('TOR_PT_SERVER_TRANSPORTS').split(',')
    
  # Returns a tuple (str,int) representing the address of the Tor server port as reported by Tor
  def getExtendedServerPort(self):
    return extendedServerPort
    
  # Returns a tuple (str,int) representing the address of the Tor OR port as reported by Tor
  def getORPort(self):
    return ORPort
    
  # Returns a dict {str: (str,int)} representing the addresses for each transport as reported by Tor
  def getServerBindAddresses(self):
    return serverBindAddr
    
  # Returns a list of strings representing the server transports reported by Tor. If present, '*' is stripped from this list and used to set allTransportsEnabled to True.
  def getServerTransports(self):
    return serverTransports

  # Write a message to stdout specifying a supported transport
  # Takes: str, (str, int), MethodOptions
  def writeMethod(self, name, address, options): # SMETHOD
    s='SMETHOD '+str(name)+' '+str(address[0])+':'+str(address[1])
    if options:
      s=s+' '+str(options)
    print(s)
    
  # Write a message to stdout specifying that an error occurred setting up the specified method
  # Takes: str, str
  def writeMethodError(self, name, message): # SMETHOD-ERROR
    print('SMETHOD-ERROR '+str(name)+' '+str(message))
    
  # Write a message to stdout specifying that the list of supported transports has ended
  def writeMethodEnd(self): # SMETHODS DONE
    print('SMETHODS DONE')

class MethodOptions:
  forward=False         # FORWARD
  args={}               # ARGS
  declare={}            # DECLARE
  useExtendedPort=False # USE-EXTENDED-PORT

  def __init__(self):
    pass

  # Sets forward to True    
  def setForward(self):
    forward=True
  
  # Adds a key-value pair to args
  def addArg(self, key, value):
    args[key]=value

  # Adds a key-value pair to declare    
  def addDeclare(self, key, value):
    declare[key]=value
    
  # Sets useExtendedPort to True
  def setUserExtendedPort(self):
    useExtendedPort=True

  def __str__(self):
    options=[]
    if forward:
      options.append('FORWARD:1')
    if len(args)>0:
      argstr='ARGS:'
      for key in args:
        value=args[key]
        argstr=argstr+key+'='+value+','
      argstr=argstr[:-1] # Remove trailing comma
      options.append(argstr)
    if len(declare)>0:
      decs='DECLARE:'
      for key in declare:
        value=args[key]
        argstr=argstr+key+'='+value+','
      decs=decs[:-1] # Remove trailing comma      
      options.append(decs)
    if useExtendedPort:
      options.append('USE-EXTENDED-PORT:1')

    return options.join(' ')      
