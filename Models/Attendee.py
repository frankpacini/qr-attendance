from mongoengine import *
from uuid import uuid4

class Attendee(DynamicDocument):
    name = StringField(required=True)
    attendeeID = UUIDField(binary=False, required=True, default=uuid4())

        