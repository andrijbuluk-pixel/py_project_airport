from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_spectacular.utils import extend_schema, OpenApiParameter

from airport_api.serializers import (
    CrewSerializer,
    AirplaneTypeSerializer,
    AirplaneSerializer,
    AirportSerializer,
    RouteSerializer,
    FlightSerializer,
    OrderSerializer,
    TicketSerializer,
)

from airport_api.models import (
    Crew,
    AirplaneType,
    Airplane,
    Airport,
    Route,
    Flight,
    Order,
    Ticket,
)

from airport_api.permissions import IsAdminOrIfAuthenticatedReadOnly


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    filter_backends = (SearchFilter, OrderingFilter,)

    search_fields = ("name",)
    ordering_fields = ("name", "rows", "id")

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "search",
                type=str,
                description="Search by aircraft name (eg ?search=Aero)",
            ),
            OpenApiParameter(
                "ordering",
                type=str,
                description="Sort results. Available fields: `name`, `rows`. To sort in descending order, add a minus (eg ?ordering=-rows)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
