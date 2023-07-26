from django.urls import path
from .views import (NewsList, detail, NewCreate, NewUpdate, NewDelete, subscriptions)

urlpatterns = [path('', NewsList.as_view(), name='news_list'),
               path('news/<str:slug>', detail, name='news_detail'),
               path('news/create/', NewCreate.as_view(), name='news_create'),
               path('news/<int:pk>/update/', NewUpdate.as_view(), name='news_update'),
               path('articles/<int:pk>/update/', NewUpdate.as_view(), name='article_update'),
               path('news/<int:pk>/delete/', NewDelete.as_view(), name='news_delete'),
               path('articles/<int:pk>/delete/', NewDelete.as_view(), name='article_delete'),
               path('subscriptions/', subscriptions, name='subscriptions')

]
