from flask import Blueprint

routes = Blueprint('routes', __name__)

# imports
from .webhook import *