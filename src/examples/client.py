#!/usr/bin/env python -u

import os
import sys

import argparse

from struct import unpack
from socket import inet_ntoa

from pyptlib.config.config import EnvException
from pyptlib.config.client import ClientConfig

class ManagedClient(Daemon):
  def __init__(self):
    try:
      Daemon.__init__(self, ClientConfig(), SocksHandler())
    except EnvException:
      print('error 0')
      return
    except UnsupportedManagedTransportVersionException:
      print('error 1')
      return
    except NoSupportedTransportsException:
      print('error 2')
      return

    try:
      self.launchClient(self.supportedTransport, 8182)
      self.config.writeMethod(self.supportedTransport, 5, ('127.0.0.1', 8182), None, None)
    except TransportLaunchException as e:
      print('error 3')
      self.config.writeMethodError(self.supportedTransport, e.message)

    self.config.writeMethodEnd()
    
    self.run()
      
  def launchClient(self, name, port):
    if name!=self.supportedTransport:
      raise TransportLaunchException('Tried to launch unsupported transport %s' % (name))

    client=DummyClient()
    self.handler.setTransport(client)
    add_service(Service(self.handler, port=port))    

if __name__=='__main__':
  server=ManagedClient()
  
