#!/usr/bin/env python

import sys
import time

from struct import unpack
from socket import inet_ntoa

import monocle
from monocle import _o, Return
monocle.init('tornado')

from monocle.stack import eventloop
from monocle.stack.network import add_service, Service, Client

from shared import pump

from config.server import ServerConfig
from daemon import Daemon

from proxy import ProxyHandler

class ManagedServer(Daemon):
  def __init__(self):
    try:
      Daemon.__init__(ServerConfig(), ProxyHandler())
    except UnsupportedManagedTransportVersionException:
      return
    except NoSupportedTransportsException:
      return

    try:
      self.launchServer(self.supportedTransport)
      self.config.writeMethod(self.supportedTransport)
    except TransportLaunchException as e:
      self.config.writeMethodError(self.supportedTransport, e.message)

    self.config.writeMethodEnd()
    
    self.run()
    
  def launchServer(self, name, port):
    if name!=self.supportedTransport:
      raise TransportLaunchException('Tried to launch unsupported transport %s' % (name))

    client=DummyServer()
    self.handler.setTransport(client)
    add_service(Service(self.handler, port=port))   
