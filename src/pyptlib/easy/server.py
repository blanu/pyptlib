#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyptlib.config import EnvException
from pyptlib.server import ServerConfig

""" The pyptlib.easy.client module provides a high-level API for implementing pluggable transport clients. """

def init(transports):
    """
        Initialize the pluggable transport by parsing the environment variables and generating output to report any errors.
        The given transports are checked against the transports enabled by Tor and a list of matching transports is returned.
        The server should then launch all of the transports in the list and report on the success or failure of those launches.
    """

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

    matchedTransports = []
    for transport in transports:
        if config.checkTransportEnabled(transport):
            matchedTransports.append(transport)

    return matchedTransports


def reportSuccess(name, address, options):
    """
        This method should be called to report when a transport has been successfully launched.
        It generates output to Tor informing that the transport launched successfully and can be used.
        After all transports have been launched, the server should call reportEnd().
    """

    config = ServerConfig()
    config.writeMethod(name, address, options)


def reportFailure(name, message):
    """
        This method should be called to report when a transport has failed to launch.
        It generates output to Tor informing that the transport failed to launch and cannot be used.
        After all transports have been launched, the server should call reportEnd().
    """

    config = ServerConfig()
    config.writeMethodError(name, message)


def reportEnd():
    """
        This method should be called after all transports have been launched.
        It generates output to Tor informing that all transports have been launched.
    """

    config = ServerConfig()
    config.writeMethodEnd()
