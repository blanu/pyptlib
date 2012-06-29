#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

import argparse

from struct import unpack
from socket import inet_ntoa

from pyptlib.config import EnvException
from pyptlib.client import ServerConfig

def init(transports):
    supportedTransportVersion = '1'
    
    try:
      config = ServerConfig()
    except EnvException:
      return []

    if config.checkManagedTransportVersion(supportedTransportVersion):
        config.writeVersion(supportedTransportVersion)
    else:
        config.writeVersionError()
        return []

    matchedTransports=[]
    for transport in transports:
      if config.checkTransportEnabled(supportedTransport):
        matchedTransports.append(transport)

    return matchedTransports

def reportSuccess(name, address, args, options):    
    config.writeMethod(name, address, options)
                           
def reportFailure(name, message):
    config.writeMethodError(name, message)

def reportEnd():
    config.writeMethodEnd()


