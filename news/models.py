from django.db import models
from django.urls import reverse


# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class New(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новости'),
        (ARTICLE, 'стастья')
    )

    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)

    title = models.CharField(max_length=128)
    text = models.TextField()
    datepost = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('detail',
                kwargs = {'slug': self.slug})




# Create your models here.
