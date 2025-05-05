from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_activation_email(user, activation_link, email, mail_subject="Confirm your email"):
    message = render_to_string("user_auth_app/email_verification.html", {
        "user": user,
        "activation_link": activation_link
    })

    send_mail(
        subject=mail_subject,
        message="",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=message,
        fail_silently=False,
    )


def generate_activation_link(user):
    token = user.token
    return f"http://localhost:4200/login?activate={user.id}&token={token}"

