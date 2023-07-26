from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import New
from django.core.mail import EmailMultiAlternatives


@receiver(post_save, sender=New)
def new_created(instance, **kwargs):
    if not kwargs['created']:
        return
    emails = User.objects.filter(
        subscriptions__category=instans.category
    ).values_list('email', flat=True)

    subject=f'Новая публикация в категории {instance.category}'

    text_content=(f'Заголовок: {instance.title}\n'
                  f'Текст: {instance.text[:20]}{"..." if len(instance.text) > 20 else ""}\n\n'
                  f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}')

    html_content=(f'Заголовок: {instance.title}<br>'
                  f'Текст: {instance.text[:20]}{"..." if len(instance.text) > 20 else ""}<br><br>'
                  f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
                  f'Ссылка на публикацию</a>')

    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()