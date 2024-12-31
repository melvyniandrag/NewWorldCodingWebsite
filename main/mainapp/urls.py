from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("comingsoon", views.coming_soon_view, name="coming_soon_view"),
    path("teaching", views.teaching_view, name="teaching_view"),
    path("horizon", views.horizon_view, name="horizon_view"),
    path("workshops/webdevelopment", views.workshop_webdevelopment_detail_view, name="workshop_webdevelopment_detail_view"),
    path("workshops/textencodings", views.workshop_textencoding_detail_view, name="workshop_textencoding_detail_view"),
    path("workshops/arduinorobot", views.workshop_arduinorobot_detail_view, name="workshop_arduinorobot_detail_view"),
    path("workshops/gameboy", views.workshop_gameboy_detail_view, name="workshop_gameboy_detail_view"),
    path("workshops/introtokotlin", views.workshop_introtokotlin_detail_view, name="workshop_introtokotlin_detail_view"),
    path("workshops/introtolinux", views.workshop_introtolinux_detail_view, name="workshop_introtolinux_detail_view"),
    path("create", views.create_view, name="create_view"),
    path("list", views.list_view, name="list_view"),
]
