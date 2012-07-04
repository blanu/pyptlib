#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyptlib.config import EnvException
from pyptlib.server import ServerConfig


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

    matchedTransports = []
    for transport in transports:
        if config.checkTransportEnabled(transport):
            matchedTransports.append(transport)

    return matchedTransports


def reportSuccess(
    name,
    address,
    options,
    ):

    config = ServerConfig()
    config.writeMethod(name, address, options)


def reportFailure(name, message):
    config = ServerConfig()
    config.writeMethodError(name, message)


def reportEnd():
    config = ServerConfig()
    config.writeMethodEnd()
