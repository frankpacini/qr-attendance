from flask import Blueprint, request, make_response
from Response import Response
from Models.Attendee import Attendee
from Models.Meeting import Meeting

home = Blueprint("HomeEndpoints", __name__, url_prefix="/api/home")

    
