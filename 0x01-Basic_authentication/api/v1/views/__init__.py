#!/usr/bin/env python3
"""Initialize Blueprint for app_views"""
from flask import Blueprint

# Create the blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import all routes for the views
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

