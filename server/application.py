import yaml
from flask import Flask
from mongoengine import connect


# Instantiate connection to database
creds = yaml.safe_load(open("creds.yaml", "r"))
dbHostUri = "mongodb+srv://" + creds["DB_USER"] + ":" + creds["DB_PASSWORD"] + \
    "@cluster0-qjnv5.mongodb.net/test?retryWrites=true&w=majority"
db = connect(host=dbHostUri)

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'

def importControllers():
    with application.app_context():
        import Controllers.AuthenticationController as auth
        import Controllers.MeetingController as meeting 
        import Controllers.HomeController as home
        import Controllers.AttendanceController as attendance
            
        application.register_blueprint(auth.auth)
        application.register_blueprint(meeting.meeting)
        application.register_blueprint(home.home)
        application.register_blueprint(attendance.attendance)

importControllers()

if __name__ == "__main__":
    application.run()