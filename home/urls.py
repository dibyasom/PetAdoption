from django.urls import include, path
from . import views

# include all urls for home
urlpatterns = [
    path("", views.AdoptionView.as_view(), name="home"),
    path(
        "application/<int:pk>", views.AdoptionApplication.as_view(), name="application"
    ),
]
