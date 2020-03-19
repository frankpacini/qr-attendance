from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'

def importControllers():
    print("Hello")
    #with application.app_context():
        # import Controllers.AdminController as admin
        # import Controllers.AuthenticationController as auth
        # import Controllers.UploadController as upload
        # import Controllers.DatasetController as dataset

        # application.register_blueprint(admin.admin)
        # application.register_blueprint(auth.auth)
        # application.register_blueprint(upload.upload)
        # application.register_blueprint(dataset.dataset)

importControllers()

if __name__ == "__main__":
    application.run()