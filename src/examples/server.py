#!/usr/bin/env python -u

import os
import sys

from struct import unpack
from socket import inet_ntoa

from pyptlib.config import EnvException
from pyptlib.server import ServerConfig, MethodOptions

supportedTransport='dummy'

def launchServer(self, name, port):
  if name!=supportedTransport:
    raise TransportLaunchException('Tried to launch unsupported transport %s' % (name))

if __name__=='__main__':
  supportedTransportVersion='1'
  config=ClientConfig()
  try:
    if config.checkManagedTransportVersion(supportedTransportVersion):
      config.writeVersion(supportedTransportVersion)
    else:
      config.writeVersionError()
      raise UnsupportedManagedTransportVersionException()
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
    launchServer(supportedTransport, 8182)
    config.writeMethod(supportedTransport, ('127.0.0.1', 8182), MethodOptions())
  except TransportLaunchException as e:
    print('error 3')
    config.writeMethodError(supportedTransport, e.message)

  config.writeMethodEnd()
