from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('deals/', views.deals, name="deals"),
    path('reservation/', views.reservation, name="reservation"),
]