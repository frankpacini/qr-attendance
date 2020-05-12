from uuid import uuid4
from Models.Meeting import Meeting
from application import db

class MeetingService:
    def __init__(self):
        return


    def createMeeting(self, name):
        meeting = Meeting(
            name=name
        )
        meeting.save()
        return meeting.meetingId