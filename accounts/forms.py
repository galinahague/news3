from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        # common_users = Group.objects.get(name='common users')
        # user.groups.add(common_users)

        subject = 'Welcome to News Portal!'
        message = f'{user.username}, you have successfully registered'
        html = (f'<b>{user.username}</b>you have successfully registered'
                f'<a href="http://127.0.0.1:8000/news">site</a>!'
                )
        msg = EmailMultiAlternatives(
            subject=subject, body=message,
            from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, 'message/html')
        msg.send()

        return user
