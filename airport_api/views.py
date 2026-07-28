from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

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


class CustomSearchFilter(SearchFilter):
    search_title = "search"
    search_description = "Text search by allowed fields (eg ?search=Aero)."


class CustomOrderingFilter(SearchFilter):
    search_title = "order"
    search_description = (
        "Sort results. To sort in descending order, add a minus (eg ?ordering=-rows)."
    )


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
    pagination_class = CustomPageNumberPagination

    filter_backends = (CustomSearchFilter,)

    search_fields = ("first_name", "last_name")
    ordering_fields = ("first_name", "last_name")


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
    pagination_class = CustomPageNumberPagination

    filter_backends = (CustomSearchFilter,)

    search_fields = ("name",)
    ordering_fields = ("name",)


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
    pagination_class = CustomPageNumberPagination

    filter_backends = (
        CustomSearchFilter,
        CustomOrderingFilter,
    )

    search_fields = ("name",)
    ordering_fields = ("name", "rows", "id")


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
    pagination_class = CustomPageNumberPagination

    filter_backends = (CustomSearchFilter,)

    search_fields = ("name", "closest_big_city")
    ordering_fields = ("name",)


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.select_related("source", "destination")
    serializer_class = RouteSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
    pagination_class = CustomPageNumberPagination


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.select_related("route", "airplane").prefetch_related("crew")
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
    pagination_class = CustomPageNumberPagination

    search_fields = (
        "route__source",
        "route__destination",
        "route__distance",
        "airplane__name",
    )
    ordering_fields = ("departure_time", "arrival_time")


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    filter_backends = (CustomSearchFilter,)

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
    )

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.select_related("flight", "order")
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    search_fields = (
        "order__user__username",
        "order__user__first_name",
        "order__user__last_name",
        "order__user__email",
    )

    def get_queryset(self):
        return Ticket.objects.filter(order__user=self.request.user)
