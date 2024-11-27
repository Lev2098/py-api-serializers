from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()

router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinemahalls", CinemaHallViewSet)
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls))
]