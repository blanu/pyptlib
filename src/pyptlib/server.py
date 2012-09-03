#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    The pyptlib.client module contains a low-level API which closely follows the Tor Proposal 180: Pluggable transports for circumvention.
    This module inherits from pyptlib.config and contains just the parts of the API which are specific to the server implementations of the protocol.
"""

import os

from pyptlib.config import Config

__docformat__ = 'restructuredtext'


class ServerConfig(Config):

    """
    The ServerConfig class contains a low-level API which closely follows the Tor Proposal 180: Pluggable transports for circumvention.
    This class inherits from pyptlib.config.Config and contains just the parts of the API which are specific to the client implementations of the protocol.
    """

    extendedServerPort = None  # TOR_PT_EXTENDED_SERVER_PORT
    ORPort = None  # TOR_PT_ORPORT
    serverBindAddr = {}  # TOR_PT_SERVER_BINADDR

  # Public methods

    def __init__(self):  # throws EnvError
        """
            Initialize the ClientConfig object.
            This causes the state location, managed transport, and transports version to be set.
        """

        Config.__init__(self)

        self.extendedServerPort = self.get('TOR_PT_EXTENDED_SERVER_PORT'
                )
        orport = self.get('TOR_PT_ORPORT').split(':')
	orport[1]=int(orport[1])
	self.ORPort=orport

        binds = self.get('TOR_PT_SERVER_BINDADDR').split(',')
        for bind in binds:
            (key, value) = bind.split('-')
            self.serverBindAddr[key] = value

        self.transports = self.get('TOR_PT_SERVER_TRANSPORTS').split(','
                )
        if '*' in self.transports:
            self.allTransportsEnabled = True
            self.transports.remove('*')

    def getExtendedServerPort(self):
        """ Returns a tuple (str,int) representing the address of the Tor server port as reported by Tor """

        return self.extendedServerPort

    def getORPort(self):
        """ Returns a tuple (str,int) representing the address of the Tor OR port as reported by Tor """

        return self.ORPort

    def getServerBindAddresses(self):
        """ Returns a dict {str: (str,int)} representing the addresses for each transport as reported by Tor """

        return self.serverBindAddr

    def getServerTransports(self):
        """ Returns a list of strings representing the server transports reported by Tor. If present, '*' is stripped from this list and used to set allTransportsEnabled to True. """

        return self.transports

    def writeMethod(  # SMETHOD
        self,
        name,
        address,
        options,
        ):
        """
        Write a message to stdout specifying a supported transport
        Takes: str, (str, int), MethodOptions
        """

        if options:
            self.emit('SMETHOD %s %s:%s %s' % (name, address[0],
                      address[1], options))
        else:
            self.emit('SMETHOD %s %s:%s' % (name, address[0],
                      address[1]))

    def writeMethodError(self, name, message):  # SMETHOD-ERROR
        """
            Write a message to stdout specifying that an error occurred setting up the specified method
            Takes: str, str
        """

        self.emit('SMETHOD-ERROR %s %s' % (name, message))

    def writeMethodEnd(self):  # SMETHODS DONE
        """ Write a message to stdout specifying that the list of supported transports has ended """

        self.emit('SMETHODS DONE')


class MethodOptions:

    """ The MethodOptions class represents the method options: FORWARD, ARGS, DECLARE, and USE-EXTENDED-PORT. """

    forward = False  # FORWARD
    args = {}  # ARGS
    declare = {}  # DECLARE
    useExtendedPort = False  # USE-EXTENDED-PORT

  # Public methods

    def setForward(self):
        """ Sets forward to True """

        self.forward = True

    def addArg(self, key, value):
        """ Adds a key-value pair to args """

        self.args[key] = value

    def addDeclare(self, key, value):
        """ Adds a key-value pair to declare """

        self.declare[key] = value

    def setUserExtendedPort(self):
        """ Sets useExtendedPort to True """

        self.useExtendedPort = True

    def __str__(self):
        """ Returns a string representation of the method options. """

        options = []
        if self.forward:
            options.append('FORWARD:1')
        if len(self.args) > 0:
            argstr = 'ARGS:'
            for key in self.args:
                value = self.args[key]
                argstr = argstr + key + '=' + value + ','
            argstr = argstr[:-1]  # Remove trailing comma
            options.append(argstr)
        if len(self.declare) > 0:
            decs = 'DECLARE:'
            for key in self.declare:
                value = self.declare[key]
                decs = decs + key + '=' + value + ','
            decs = decs[:-1]  # Remove trailing comma
            options.append(decs)
        if self.useExtendedPort:
            options.append('USE-EXTENDED-PORT:1')

        return ' '.join(options)


