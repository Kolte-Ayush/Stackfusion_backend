from django.core.mail import send_mail, EmailMessage
from Stack_Fusion.settings import EMAIL_HOST_USER, BASE_DIR
from string import Template
from .EmailBuilder import EmailBuilder


class EmailService:

    @staticmethod
    def send(msg):
        text = EmailBuilder.content()
        email = EmailMessage(msg.subject, text, msg.frm, msg.to)
        email.content_subtype = "html"
        try:
            res = email.send()
        except Exception as e:
            res = e
        return res
