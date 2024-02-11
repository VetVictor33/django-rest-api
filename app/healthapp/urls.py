"""Healthapp urls config
"""

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('health/', views.getData),
    path('health/post', views.postData),
]