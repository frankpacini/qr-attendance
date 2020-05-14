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
    meeting = MeetingService.getMeeting(meetingID)
    if(meeting == None):
        return Response("No meeting", status=400)
    
    print(meeting)
    print("Id: " + str(meeting.meetingID))
    return Response({"meetingID": str(meeting.meetingID), "name" : meeting.name, "active" : meeting.active}, status=200)

@meeting.route("/<meetingID>", methods=["POST"])
def closeMeeting(meetingID):
    print("Hello2")
    active = MeetingService.closeMeeting(meetingID)
    if(not active):
        return Response({"active" : active}, status=200)
    else:
        return Response("Meeting not found", status = 400)
        
    