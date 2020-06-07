#from cattlea.apps.orders.models import Order 
from .main import EmailMain

def email_register(user):

    subject = "Welcome to Cattlea!"
    message =  "authentication/email-register.html" # f"Hi {user.first_name}! You have successfully registered"
    context = {"user": user.first_name}
    reciever = [user.email]

    email = EmailMain(
        subject=subject,
        message=message,
        context=context,
        reciever=reciever
    )

    email.send()


def email_order(user, order):

    subject = "Order from Cattlea"
    message = "orders/email_order.html"

    context = {
        "user": user,
        "order": order
    }

    reciever = [user.email]

    email = EmailMain(
        subject=subject,
        message=message,
        context=context,
        reciever=reciever
    )

    email.send()


def email_delivery(user, order):

    subject = "Order is Out for Delivery"
    message = "orders/email_delivery.html"

    context = {
        "user": user,
        "order": order
    }

    reciever = [user.email]

    email = EmailMain(
        subject=subject,
        message=message,
        context=context,
        reciever=reciever
    )

    email.send()


def email_received(user, order):

    subject = "Order is Delivered!"
    message = "orders/email_received.html"

    context = {
        "user": user,
        "order": order
    }

    reciever = [user.email]

    email = EmailMain(
        subject=subject,
        message=message,
        context=context,
        reciever=reciever
    )

    email.send()
