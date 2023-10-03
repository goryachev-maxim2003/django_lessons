from django.urls import path

from . import views

urlpatterns = [
    path("", views.DjabaView.as_view())
]