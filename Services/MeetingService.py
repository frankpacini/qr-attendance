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
        return meeting.meetingID

    def getMeeting(self, id):
        #checks if there is a meeting in the database with the meeting id, if there is then it returns the 
        print("ID: " + str(id))
        meeting = Meeting.objects(meetingID=id).first() 
        return meeting  