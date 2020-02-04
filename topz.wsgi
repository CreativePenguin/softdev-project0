#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/topz/")
sys.path.insert(0,"/var/www/topz/topz/")

import logging
logging.basicConfig(stream=sys.stderr)

from topz import app as application
