#!/usr/bin/env python -u

import sys
import time

from struct import unpack
from socket import inet_ntoa

import monocle
from monocle import _o, Return
monocle.init('tornado')

from monocle.stack import eventloop
from monocle.stack.network import add_service, Service, Client, ConnectionLost
from pyptlib.framework.loopback import FakeSocket

from pyptlib.framework.socks import SocksHandler

from pyptlib.config.client import ClientConfig
from pyptlib.framework.daemon import *

class ManagedClient(Daemon):
  def __init__(self):
    try:
      Daemon.__init__(self, ClientConfig(), SocksHandler())
    except UnsupportedManagedTransportVersionException:
      return
    except NoSupportedTransportsException:
      return

    try:
      self.launchClient(self.supportedTransport)
      self.config.writeMethod(self.supportedTransport)
    except TransportLaunchException as e:
      self.config.writeMethodError(self.supportedTransport, e.message)

    self.config.writeMethodEnd()
    
    self.run()
      
  def launchClient(self, name, port):
    if name!=self.supportedTransport:
      raise TransportLaunchException('Tried to launch unsupported transport %s' % (name))

    client=DummyClient()
    self.handler.setTransport(client)
    add_service(Service(self.handler, port=port))    
