import sys
import time

from struct import unpack
from socket import inet_ntoa

import monocle
from monocle import _o, Return
monocle.init('tornado')

from monocle.stack import eventloop
from monocle.stack.network import add_service, Service, Client

from shared import pump

@_o
def handle_proxy(conn):
  print('connection')
  client = Client()
  yield client.connect('blanu.net', 7051)

  coder=yield handshake(client)

  monocle.launch(pump, conn, client, coder.encrypt)
  yield pump(client, conn, coder.decrypt)

add_service(Service(handle_proxy, port=7050))
eventloop.run()
