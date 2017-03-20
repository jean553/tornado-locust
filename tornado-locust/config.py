"""
Get the configuration from the environment variable
"""

import os

PROJECT = os.environ.get("PROJECT")
TORNADO_PORT = os.environ.get("TORNADO_PORT")
