from django.urls import path

from Pages.views import home, contact, about

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about")
]
