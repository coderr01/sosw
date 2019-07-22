"""Sosw Essential Scavenger
"""

import logging

from sosw.scavenger import Scavenger
from sosw.app import LambdaGlobals, get_lambda_handler

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Essential(Scavenger):
    pass


global_vars = LambdaGlobals()
lambda_handler = get_lambda_handler(Essential, global_vars)
