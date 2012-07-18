#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    The pyptlib.config module contains a low-level API which closely follows the Tor Proposal 180: Pluggable transports for circumvention.
    This module contains the parts of the API which are shared by both client and server implementations of the protocol.
"""

import os
import logging

__docformat__ = 'restructuredtext'


class Config:

    """
    The Config module class a low-level API which closely follows the Tor Proposal 180: Pluggable transports for circumvention.
    This class contains the parts of the API which are shared by both client and server implementations of the protocol.
    """

    stateLocation = None  # TOR_PT_STATE_LOCATION
    managedTransportVer = []  # TOR_PT_MANAGED_TRANSPORT_VER
    transports = []  # TOR_PT_SERVER_TRANSPORTS or TOR_PT_CLIENT_TRANSPORTS
    allTransportsEnabled = False

  # Public methods

    def __init__(self):  # throws EnvError
        """ Initialize the Config object. this causes the state location and managed transport version to be set. """

        self.stateLocation = self.get('TOR_PT_STATE_LOCATION')
        self.managedTransportVer = \
            self.get('TOR_PT_MANAGED_TRANSPORT_VER').split(',')

    def checkClientMode(self):
        """ Check to see if the daemon is being run as a client or a server. This is determined by looking for the presence of the TOR_PT_CLIENT_TRANSPORTS environment variable. """

        return self.check('TOR_PT_CLIENT_TRANSPORTS')

    def getStateLocation(self):
        """ Return the state location, a string representing the path to the state storage directory (which may not exist, but should be creatable) reported by Tor. """

        return self.stateLocation

    def getManagedTransportVersions(self):
        """ Return the managed transport versions, a list of strings representing supported versions as reported by Tor. """

        return self.managedTransportVer

    def checkManagedTransportVersion(self, version):
        """
            Checks to see if the specified version is included in those reported by Tor
            Returns True if the version is included and False if it is not
        """

        return version in self.managedTransportVer

    def getAllTransportsEnabled(self):
        """ Returns a bool, True if the transport '*' was specified by Tor, otherwise False. """

        return self.allTransportsEnabled

    def checkTransportEnabled(self, transport):
        """ Returns a bool, True if either the given transport or the transport '*' was specified by Tor, otherwise False. """

        return self.allTransportsEnabled or transport in self.transports

    def writeEnvError(self, message):  # ENV-ERROR
        """
            Write a message to stdout specifying that an error parsing the environment variables has occurred
            Takes: str
        """

        self.emit('ENV-ERROR %s' % message)

    def writeVersion(self, version):  # VERSION
        """
            Write a message to stdout specifying that the specified configuration protocol version is supported
            Takes: str
        """

        self.emit('VERSION %s' % version)

    def writeVersionError(self):  # VERSION-ERROR
        """
            Write a message to stdout specifying that none of the specified configuration protocol versions are supported
        """

        self.emit('VERSION-ERROR no-version')

 # Private methods

    def check(self, key):
        """ Returns True if the specified environment variable is set, otherwise returns False. """

        return key in os.environ

    def get(self, key):
        """ Attempts to fetch the given key from the environment variables. If it is present, it is returned, otherwise an EnvException is thrown. """

        if key in os.environ:
            return os.environ[key]
        else:
            message = 'Missing environment variable %s' % key
            self.writeEnvError(message)
            raise EnvException(message)

    def emit(self, msg):
        print msg
        logging.error(msg)


# Exception thrown when there is an error parsing the configuration parameters provided by Tor in environment variables

class EnvException(Exception):

    """ The EnvException exception is thrown whenever a required environment variable is not presented or cannot be parsed. """

    message = None

    def __init__(self, message):
        self.message = message


