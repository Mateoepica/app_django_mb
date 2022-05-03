
from django.contrib import admin
from django.urls import path, include
from myapp.dash_apps.finished_apps import simpleexample
from . import views

urlpatterns = [
    path('', views.login),
    # path('login', views.login),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('after_login', views.after),
]
