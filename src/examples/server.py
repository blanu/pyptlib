#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This is an example server which shows how to call the pyptlib.easy high-level API. """

from pyptlib.easy.server import init, reportSucess, reportFailure, \
    reportEnd


class TransportLaunchException(Exception):

    pass


def launchServer(self, name, port):
    if name != 'dummy':
        raise TransportLaunchException('Tried to launch unsupported transport %s'
                 % name)


if __name__ == '__main__':
    supportedTransports = ['dummy', 'rot13']

    matchedTransports = init(supportedTransports)
    for transport in matchedTransports:
        try:
            launchServer(transport, 8182)
            reportSuccess(transport, ('127.0.0.1', 8182), None)
        except TransportLaunchException:
            reportFailure(transport, 'Failed to launch')
    reportEnd()
