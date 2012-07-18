#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyptlib.config import Config, EnvException

def checkClientMode():
    try:
        c = Config()
        return c.checkClientMode() 
    except EnvException:
        return False
