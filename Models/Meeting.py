from mongoengine import *
from Models.Attendee import Attendee
import uuid

class Meeting(DynamicDocument):
    name = StringField(required=True)
    meetingID = UUIDField(binary=False, required=True, default=uuid.uuid4, unique=True)
    attendees = ListField(ReferenceField(Attendee))
    active = BooleanField(required=True,default=True)
    
