#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:46:57 2020

@author: hannousse
"""

import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler

def NsLog(modulename):

    logFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logFileName = "../log/{}.log".format(modulename)
    logHandler = TimedRotatingFileHandler(logFileName, when="midnight")
    logHandler.setFormatter(logFormatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(logFormatter)
    logger = logging.getLogger(logFileName)

    for h in logger.handlers:
        logger.removeHandler(h)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(logHandler)
    logger.addHandler(streamHandler)

    return logger

def txt_to_list(txt_object):
    list = []

    for line in txt_object:
        list.append(line.strip())
    txt_object.close()
    return list