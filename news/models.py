from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                            related_name='subscriptions',)
    category = models.ForeignKey(to='Сategory', on_delete=models.CASCADE,
                                 related_name='subscriptions',)



class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()


class New(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новости'),
        (ARTICLE, 'стастья')
    )

    categoryType = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default=ARTICLE)

    title = models.CharField(max_length=128)
    text = models.TextField()
    date_post = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('detail',
                        kwargs ={'slug': self.slug})




# Create your models here.
