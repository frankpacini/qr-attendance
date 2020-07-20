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


@meeting.route("/names/<meetingID>", methods=["GET"])
def getNames(meetingID):
    meeting = MeetingService.getMeeting(meetingID)
    attendees = meeting.attendees 
    names = []
    for attendee in attendees:
        names.append(str(attendee.name))
    return Response({"names": names})

@meeting.route("/<meetingID>", methods=["POST"])
def closeMeeting(meetingID):
    print("Hello2")
    active = MeetingService.closeMeeting(meetingID)
    if(not active):
        return Response({"active" : active}, status=200)
    else:
        return Response("Meeting not found", status = 400)



@meeting.route("/<meetingID>", methods=["GET"])
def getMeeting(meetingID):
    dict = getMeetingDict(meetingID)
    if(meeting == None):
        return Response("No meeting", status=400)
    print(dict)
    print("Id: " + dict["meetingID"])
    return Response(dict, status=200)

@meeting.route("/all", methods=["GET"])
def getAllMeetings():
    meetings = MeetingService.getAllMeetings()
    ids = []
    meeting_dict = {}
    meeting_dict["dict"] = {}
    for meeting in meetings:
        id = str(meeting.meetingID)
        ids.append(id)
        meeting_dict["dict"][id] = getMeetingDict(id)
    meeting_dict["ids"] = ids
    return Response(meeting_dict, status=200)

def getMeetingDict(id): 
    meeting = MeetingService.getMeeting(id)
    if meeting == None:
        return None
    return {"meetingID": str(meeting.meetingID), "name" : meeting.name, "active" : meeting.active}
        
    