from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import views to register them with the blueprint
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

