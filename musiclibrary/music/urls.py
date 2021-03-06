from typing import ValuesView
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>/', views.SongDetail.as_view())
]