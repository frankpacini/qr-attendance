from uuid import uuid4
from Models.Attendee import Attendee
from Models.Meeting import Meeting
from application import db

class AttendanceService:
    def __init__(self):
        return

    def createAttendee(self, name):
        attendee = Attendee(
            name = name
        )
        attendee.save()
        return attendee

    def attendMeeting(self, attendee, meetingID):
        meeting = Meeting.objects(meetingID=meetingID).first()
        if(meeting.active and not meeting in attendee.meetings):
            meeting.attendees.append(attendee)
            meeting.save()
            attendee.meetings.append(meeting)
            attendee.save()

    def updateName(self, name, userID):
        print("userID " + str(userID))
        user = Attendee.objects(attendeeID=userID).first()
        user.name = name
        user.save()
        return user