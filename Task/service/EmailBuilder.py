from Stack_Fusion.settings import EMAIL_HOST_USER, BASE_DIR
from string import Template


class EmailBuilder:

    @staticmethod
    def content():
        message = ""
        message += "<HTML><BODY>"
        message += "<H1>Thank You</H1>"
        message += "Registration is Successfully"
        message += "<H1>Hi! Greetings from Us!</H1>"
        return message
