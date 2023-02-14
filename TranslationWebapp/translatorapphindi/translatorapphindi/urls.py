
from django.contrib import admin
from django.urls import path
from core.views import translateapp



urlpatterns = [
    path(' ', translateapp, name='trans')
]
