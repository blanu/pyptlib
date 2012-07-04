#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyptlib.config import EnvException
from pyptlib.client import ClientConfig


def init(transports):
    supportedTransportVersion = '1'

    try:
        config = ClientConfig()
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
    socksVersion,
    address,
    args,
    optArgs,
    ):

    config = ClientConfig()
    config.writeMethod(name, socksVersion, address, args, optArgs)


def reportFailure(name, message):
    config = ClientConfig()
    config.writeMethodError(name, message)


def reportEnd():
    config = ClientConfig()
    config.writeMethodEnd()


