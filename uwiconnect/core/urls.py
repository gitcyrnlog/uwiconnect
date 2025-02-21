from django.urls import path 
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("features/", views.features, name = "features"),
    path("pricing/", views.pricing, name="pricing"),
    path("help/", views.help, name="help"),
    path("safety/", views.safety, name="safety")


]