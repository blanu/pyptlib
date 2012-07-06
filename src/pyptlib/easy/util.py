#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyptlib.config import EnvException
from pyptlib.client import ClientConfig


def checkClientMode():
    try:
        client = ClientConfig()
        return True
    except EnvException:
        return False


