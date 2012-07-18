#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging

__docformat__ = 'restructuredtext'


class Config:

    stateLocation = None  # TOR_PT_STATE_LOCATION
    managedTransportVer = []  # TOR_PT_MANAGED_TRANSPORT_VER
    transports = []  # TOR_PT_SERVER_TRANSPORTS or TOR_PT_CLIENT_TRANSPORTS
    allTransportsEnabled = False

  # Public methods

    def __init__(self):  # throws EnvError
        self.stateLocation = self.get('TOR_PT_STATE_LOCATION')
        self.managedTransportVer = \
            self.get('TOR_PT_MANAGED_TRANSPORT_VER').split(',')

    def checkClientMode(self):
        return self.check('TOR_PT_CLIENT_TRANSPORTS')

  # Returns a string representing the path to the state storage directory (which may not exist, but should be creatable) reported by Tor

    def getStateLocation(self):
        return self.stateLocation

  # Returns a list of strings representing supported versions as reported by Tor

    def getManagedTransportVersions(self):
        return self.managedTransportVer

  # Checks to see if the specified version is included in those reported by Tor
  # Returns True if the version is included and False if it is not

    def checkManagedTransportVersion(self, version):
        return version in self.managedTransportVer

  # Returns a bool, True if the transport '*' was specified by Tor, otherwise False.

    def getAllTransportsEnabled(self):
        return self.allTransportsEnabled

    def checkTransportEnabled(self, transport):
        return self.allTransportsEnabled or transport in self.transports

  # Write a message to stdout specifying that an error parsing the environment variables has occurred
  # Takes: str

    def writeEnvError(self, message):  # ENV-ERROR
        self.emit('ENV-ERROR %s' % message)

  # Write a message to stdout specifying that the specified configuration protocol version is supported
  # Takes: str

    def writeVersion(self, version):  # VERSION
        self.emit('VERSION %s' % version)

  # Write a message to stdout specifying that none of the specified configuration protocol versions are supported

    def writeVersionError(self):  # VERSION-ERROR
        self.emit('VERSION-ERROR no-version')

 # Private methods

    def check(self, key):
        return key in os.environ

    def get(self, key):
        if key in os.environ:
            return os.environ[key]
        else:
            message = 'Missing environment variable %s' % key
            self.writeEnvError(message)
            raise EnvException(message)

    def emit(self, msg):
      print(msg)
      logging.error(msg)

# Exception thrown when there is an error parsing the configuration parameters provided by Tor in environment variables

class EnvException(Exception):

    message = None

    def __init__(self, message):
        self.message = message


