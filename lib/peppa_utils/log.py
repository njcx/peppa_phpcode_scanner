# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : log.py

import time
import logging.handlers


class Logger(object):
    now = time.strftime('%Y-%m-%d')
    log_file = LOG_PATH + 'peppa-nids-' + now + '.log'
    log_level = logging.DEBUG
    log_max_byte = 100 * 1024 * 1024;
    log_backup_count = 10

    @staticmethod
    def get_logger(name="Logger"):

        logger = logging.Logger(name)
        std_out = logging.StreamHandler()
        log_handler = logging.handlers.RotatingFileHandler(filename=Logger.log_file, \
                                                           maxBytes=Logger.log_max_byte, \
                                                           backupCount=Logger.log_backup_count)

        log_fmt = logging.Formatter('%(asctime)s -%(name)s- %(lineno)d- %(process)d- '
                                    '%(funcName)s- %(levelname)s - %(message)s')

        std_out.setFormatter(log_fmt)
        log_handler.setFormatter(log_fmt)

        logger.addHandler(log_handler)
        logger.addHandler(std_out)

        logger.setLevel(Logger.log_level)
        return logger


if __name__ == "__main__":

    test = Logger.get_logger(__name__)
    test.error("xxx")
