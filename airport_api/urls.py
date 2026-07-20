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

router.register("crew", CrewViewSet)
router.register("type", AirplaneTypeViewSet)
router.register("airplane", AirplaneViewSet)
router.register("airport", AirportViewSet)
router.register("route", RouteViewSet)
router.register("flight", FlightViewSet)
router.register("order", OrderViewSet)
router.register("ticket", TicketViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "airport_api"
