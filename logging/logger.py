#!/usr/bin/env python3
# -*-coding: utf8 -*-

import logging

_log_format = f'%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
#_log_format = f'%(asctime)s - [%(levelname)s] - %(funcName)s(%(lineno)d) - %(message)s'


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("./log.log")
    file_handler.setLevel(logging.INFO)

    #_log_format = f'%(asctime)s - [%(levelname)s] - %(funcName)s(%(lineno)d) - %(message)s'
    _log_format = f'%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
    file_handler.setFormatter(logging.Formatter(_log_format))

    logger.addHandler(file_handler)
    return logger
