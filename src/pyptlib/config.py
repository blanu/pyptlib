class Config:
  stateLocation=None     # TOR_PT_STATE_LOCATION
  managedTransportVer=[] # TOR_PT_MANAGED_TRANSPORT_VER
  allTransportsEnabled=False
  
  def __init__(self): # throws EnvError
    pass
    
  # Returns a string representing the path to the state storage directory (which may not exist, but should be creatable) reported by Tor
  def getStateLocation(self):
    return stateLocation

  # Returns a list of strings representing supported versions as reported by Tor    
  def getManagedTransportVersions(self)
    return managedTransportVer
    
  # Checks to see if the specified version is included in those reported by Tor
  # Returns True if the version is included and False if it is not
  def checkManagedTransportVersion(self, version):
    pass

  # Returns a bool, True if the transport '*' was specified by Tor, otherwise False.
  def getAllTransportsEnabled(self):
    return allTransportsEnabled

# Exception thrown when there is an error parsing the configuration parameters provided by Tor in environment variables    
class EnvException(Exception):
  pass
