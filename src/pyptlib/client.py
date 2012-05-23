class ClientConfig(Config):
  clientTransports=[] # TOR_PT_CLIENT_TRANSPORTS
  
  def __init__(self): # throws EnvError
    Config.__init__(self)
    
  # Returns a list of strings representing the client transports reported by Tor. If present, '*' is stripped from this list and used to set allTransportsEnabled to True.
  def getClientTransports():
    return clientTransports

  # Write a message to stdout specifying a supported transport
  # Takes: str, int, (str, int), [str], [str]
  def writeMethod(name, socksVersion, address, args, optArgs): # CMETHOD
    pass
    
  # Write a message to stdout specifying that an error occurred setting up the specified method
  # Takes: str, str
  def writeMethodError(name, message): # CMETHOD-ERROR
    pass
    
  # Write a message to stdout specifying that the list of supported transports has ended
  def writeMethodEnd() # CMETHODS DONE
    pass
