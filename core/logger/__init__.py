import logging

_logger = logging.getLogger("system")


def logger(level_name: str, extra: dict, message: str = None):
    level = logging.getLevelName(level_name)
    if message:
        _logger.log(level, message, extra=extra)
    else:
        _logger.log(level, "", extra=extra)
