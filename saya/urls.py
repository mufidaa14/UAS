from django.urls import path
from . import views

urlpatterns = [
    path("haii/", views.haii, name="haii"),
    path("pendaftaran_form", views.pendaftaran_form, name="pendaftaran_form"),
]