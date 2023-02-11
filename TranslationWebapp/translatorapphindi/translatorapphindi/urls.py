
from django.contrib import admin
from django.urls import path
from core.views import translate_app



urlpatterns = [
    path('admin/', admin.site.urls),
    path('translate',translate_app , name='trans')
]
