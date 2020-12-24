from django.urls import path
from .views import contactMeView, mainPageView

urlpatterns = [
    path('', mainPageView, name="index"),
    path('contact', contactMeView, name="contactMe"),
]