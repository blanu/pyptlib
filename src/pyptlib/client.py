#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    The pyptlib.client module contains a low-level API which closely follows the Tor Proposal 180: Pluggable transports for circumvention.
    This module inherits from pyptlib.config and contains just the parts of the API which are specific to the client implementations of the protocol.
"""

import os

from pyptlib.config import Config

__docformat__ = 'restructuredtext'


class ClientConfig(Config):
"""
    The ClientConfig class contains a low-level API which closely follows the Tor Proposal 180: Pluggable transports for circumvention.
    This class inherits from pyptlib.config.Config and contains just the parts of the API which are specific to the client implementations of the protocol.
"""

  # Public methods

    def __init__(self):  # throws EnvError
        """
            Initialize the ClientConfig object.
            This causes the state location, managed transport, and transports version to be set.
        """

        Config.__init__(self)

        self.transports = self.get('TOR_PT_CLIENT_TRANSPORTS').split(','
                )
        if '*' in self.transports:
            self.allTransportsEnabled = True
            self.transports.remove('*')

    def getClientTransports(self):
        """ Returns a list of strings representing the client transports reported by Tor. If present, '*' is stripped from this list and used to set allTransportsEnabled to True. """

        return self.transports

    def writeMethod(  # CMETHOD
        self,
        name,
        socksVersion,
        address,
        args,
        optArgs,
        ):
        """
            Write a message to stdout specifying a supported transport
            Takes: str, int, (str, int), [str], [str]
        """

        methodLine = 'CMETHOD %s socks%s %s:%s' % (name, socksVersion,
                address[0], address[1])
        if args and len(args) > 0:
            methodLine = methodLine + ' ARGS=' + args.join(',')
        if optArgs and len(optArgs) > 0:
            methodLine = methodLine + ' OPT-ARGS=' + args.join(',')
        self.emit(methodLine)

    def writeMethodError(self, name, message):  # CMETHOD-ERROR
        """
            Write a message to stdout specifying that an error occurred setting up the specified method
            Takes: str, str
        """

        self.emit('CMETHOD-ERROR %s %s' % (name, message))

    def writeMethodEnd(self):  # CMETHODS DONE
        """ Write a message to stdout specifying that the list of supported transports has ended """

        self.emit('CMETHODS DONE')
