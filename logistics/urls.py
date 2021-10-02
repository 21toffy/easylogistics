from django.urls import path
from .views import LandingPage

app_name = "logistics"


urlpatterns = [
    path("", LandingPage.as_view(), name="landing"),

]