from mongoengine import *

class Attendee(DynamicDocument):
    name = StringField(required=True)
    attendeeID = UUIDField(binary=False, required=True)

        