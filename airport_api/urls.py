from django.urls import path, include
from rest_framework import routers

from airport_api.views import (
    CrewViewSet,
    AirplaneTypeViewSet,
    AirplaneViewSet,
    AirportViewSet,
    RouteViewSet,
    FlightViewSet,
    OrderViewSet,
    TicketViewSet,
)

router = routers.DefaultRouter()

router.register("crew", CrewViewSet, basename="crew")
router.register("type", AirplaneTypeViewSet, basename="type")
router.register("airplane", AirplaneViewSet, basename="airplane")
router.register("airport", AirportViewSet, basename="airport")
router.register("route", RouteViewSet, basename="route")
router.register("flight", FlightViewSet, basename="flight")
router.register("order", OrderViewSet, basename="order")
router.register("ticket", TicketViewSet, basename="ticket")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "airport_api"
