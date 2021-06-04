from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.welcomefunc),
    path('hello',views.hello)
]
