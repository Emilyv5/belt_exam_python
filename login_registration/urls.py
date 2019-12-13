from django.urls import path
from . import views
import handy_helper

urlpatterns = [
    path('', views.index),
    path('addition', views.addition),
    path('check', views.check),
]
