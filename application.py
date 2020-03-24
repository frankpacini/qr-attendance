import yaml
from flask import Flask
from mongoengine import connect


# Instantiate connection to database
creds = yaml.safe_load(open("creds.yaml", "r"))
dbHostUri = "mongodb+srv://" + creds["DB_USER"] + ":" + creds["DB_PASSWORD"] + \
    "@cluster0-ollas.mongodb.net/test?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
db = connect(host=dbHostUri)

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'

def importControllers():
    with application.app_context():
        # import Controllers.AdminController as admin
        import Controllers.AuthenticationController as auth
        # import Controllers.UploadController as upload
        # import Controllers.DatasetController as dataset

        #application.register_blueprint(admin.admin)
        application.register_blueprint(auth.auth)
        # application.register_blueprint(upload.upload)
        # application.register_blueprint(dataset.dataset)

importControllers()

if __name__ == "__main__":
    application.run()