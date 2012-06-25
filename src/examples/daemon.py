#!/usr/bin/env python

import sys
import time

from struct import unpack
from socket import inet_ntoa

class Daemon:
  config=None
  handler=None
  
  supportedTransportVersion='1'
  supportedTransport='dummy'

  def __init__(self, configManager, handler):
    self.config=configManager
    self.handler=handler
    
    if self.config.checkManagedTransportVersion(self.supportedTransportVersion):
      self.config.writeVersion(self.supportedTransportVersion)
    else:
      self.config.writeVersionError()
      raise UnsupportedManagedTransportVersionException()
        
    if not self.config.checkTransportEnabled(self.supportedTransport):
      raise NoSupportedTransportsException()
  
  def run(self):
    eventloop.run()
    
class UnsupportedManagedTransportVersionException(Exception):
  pass

class NoSupportedTransportsException(Exception):
  pass

class TransportLaunchException(Exception):
  def __init__(self, message):
    self.message=message
  
