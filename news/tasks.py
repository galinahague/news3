from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Subscription, New
from datetime import timedelta, time
from django.template.loader import render_to_string


@shared_task
def send_weekly_newsletter():
    now = timezone.now()
    current_day_of_week = now.weekday()

    if current_day_of_week == 0 and now.time() >= time(hour=8):
        last_monday = now.date() - timedelta(days=7)
        start_time = timezone.make_aware(timezone.datetime.combine(last_monday, time(hour=8)))
        subscriptions = Subscription.objects.all()

        news_and_articles = New.objects.filter(date_post__gte=start_time)

        for subscription in subscriptions:
            html_message = render_to_string('mail.html', {'news_and_articles': news_and_articles})
            send_mail(
                'Еженедельная рассылка новостей и статей',
                'отправитель@example.com',
                [subscription.user.email],
                fail_silently=False,
                html_message=html_message,

            )