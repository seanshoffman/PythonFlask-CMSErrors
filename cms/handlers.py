## Imports
from flask import request, render_template

from cms import app
from cms.admin.models import Content, Type

from logging import getLogger
#!

request_log = getLogger('werkzeug')

request_log.disabled = True

def configure_logging(name, level):
    log = getLogger(name)
    log.setLevel(level)

