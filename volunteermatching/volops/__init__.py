from flask import Blueprint

bp_volops = Blueprint('volops', __name__, template_folder="templates")

from .models import Partner, Opportunity, Passion, AgeGroupInterest, \
    Skill, Frequency
from . import views, forms
