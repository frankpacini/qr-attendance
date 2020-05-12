from flask import Blueprint, request, make_response
from Response import Response
from Models.Attendee import Attendee
from Models.Meeting import Meeting

attendance = Blueprint("AttendanceEndpoints", __name__, url_prefix="/api/attendance")

@attendance.route("/", methods=["GET"])
def get():
    print("You are here")
    #I don't know maybe create the Meeting model and pass it the id
    

@attendance.route("/<attendance_id>", methods=["POST"])
def recordAttendance(attendance_id):
    #record that the person is attending the specific meeting 
    return "Hello"