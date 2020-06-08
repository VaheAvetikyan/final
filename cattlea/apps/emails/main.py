from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from cattlea import settings

class EmailMain:

    sender = settings.EMAIL_HOST_USER

    def __init__(self, subject, message, context, reciever):
        self.subject = subject

        html_message = render_to_string(message, context)
        plain_message = strip_tags(html_message)
        self.message = plain_message

        self.reciever = reciever

    def send(self):
        send_mail(
            self.subject,
            self.message,
            self.sender,
            self.reciever,
        )
