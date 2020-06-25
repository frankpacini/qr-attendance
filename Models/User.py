from mongoengine import (DynamicDocument, Document, StringField, EmailField, ListField, ValidationError, BooleanField)

class User(DynamicDocument):
    email = EmailField(required=True)
    password = StringField(required=True)