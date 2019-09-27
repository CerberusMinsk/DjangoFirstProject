from django.urls import path

from .views import *


urlpatterns = [
    path('', hello),
    path('1/', posts_list),
]
