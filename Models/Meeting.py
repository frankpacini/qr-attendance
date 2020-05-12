from mongoengine import *
from Models.Attendee import Attendee
from uuid import uuid4

class Meeting(DynamicDocument):
    name = StringField(required=True)
    meetingId = UUIDField(binary=False, required=True, default=uuid4())
    attendees = ListField(ReferenceField(Attendee))
    
