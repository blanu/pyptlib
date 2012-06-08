#!/usr/bin/env python

import sys
import time

from struct import unpack
from socket import inet_ntoa

import monocle
from monocle import _o, Return
monocle.init('tornado')

from monocle.stack import eventloop
from monocle.stack.network import add_service, Service, Client, ConnectionLost
from loopback import FakeSocket

from shared import *
from socks import *

class Daemon:
  config=None
  handler=None
  
  supportedTransportVersion='1'
  supportedTransport='dummy'

  def __init__(self, configManager, handler):
    self.config=configManager
    self.handler=handler
    
    if self.config.checkManagedTransportVersion(supportedTransportVersion):
      self.config.writeVersion(supportedTransportVersion)
    else:
      self.config.writeVersionError()
      raise UnsupportedManagedTransportVersionException()
        
    if not self.config.checkTransportEnabled(supportedTransport):
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
  