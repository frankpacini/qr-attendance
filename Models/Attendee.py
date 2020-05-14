from mongoengine import *
import uuid

class Attendee(DynamicDocument):
    name = StringField(required=True)
    attendeeID = UUIDField(binary=False, required=True, default=uuid.uuid4, unique=True)

        