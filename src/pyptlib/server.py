class ServerConfig(Config):
  extendedServerPort=None # TOR_PT_EXTENDED_SERVER_PORT
  ORPort=None             # TOR_PT_ORPORT
  serverBindAddr={}       # TOR_PT_SERVER_BINADDR
  serverTransports=[]     # TOR_PT_SERVER_TRANSPORTS
  
  def __init__(self): # throws EnvError
    Config.__init__(self)
    
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

  # Write a message to stdout specifying that an error parsing the environment variables has occurred
  # Takes: str
  def writeEnvError(self, message): # ENV-ERROR
    pass

  # Write a message to stdout specifying that the specified configuration protocol version is supported   
  # Takes: str
  def writeVersion(self, version): # VERSION
    pass
    
  # Write a message to stdout specifying a supported transport
  # Takes: str, (str, int), MethodOptions
  def writeMethod(self, name, address, options): # SMETHOD
    pass
    
  # Write a message to stdout specifying that an error occurred setting up the specified method
  # Takes: str, str
  def writeMethodError(self, name, message): # SMETHOD-ERROR
    pass    
    
  # Write a message to stdout specifying that the list of supported transports has ended
  def writeMethodEnd(self) # SMETHODS DONE
    pass

class MethodOptions:
  forward=False         # FORWARD
  args={}               # ARGS
  declare={}            # DECLARE
  useExtendedPort=False # USE-EXTENDED-PORT

  def __init__(self):
    pass

  # Sets forward to True    
  def setForward(self)
    pass
  
  # Adds a key-value pair to args
  def addArg(self, key, value):
    pass

  # Adds a key-value pair to declare    
  def addDeclare(self, key, value):
    pass
    
  # Sets useExtendedPort to True
  def setUserExtendedPort(self)
    pass
