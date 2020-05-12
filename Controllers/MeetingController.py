from flask import Blueprint, request, make_response
from Response import Response
from pymongo import MongoClient
from Models.Attendee import Attendee
from Models.Meeting import Meeting
from Services.MeetingService import MeetingService

MeetingService = MeetingService()

meeting = Blueprint("meetingEndpoints", __name__, url_prefix="/api/meeting")


@meeting.route("/createMeeting", methods=["POST"])
def createMeeting():
    print("This is running")
    #take in a meeting name and create a new meeting
    print(request.form)
    name = request.form["name"]
    meetingID = MeetingService.createMeeting(name)
    return {"meetingID": str(meetingID)}    



@meeting.route("/<meetingID>", methods=["GET"])
def getMeeting(meetingID):
    return "Meeting"