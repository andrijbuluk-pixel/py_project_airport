from rest_framework import serializers

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


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = (
            "id",
            "name",
        )


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = (
            "id",
            "name",
            "image",
            "rows",
            "seats_in_row",
            "airplane_type",
        )


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = (
            "id",
            "name",
            "closest_big_city",
        )


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            "id",
            "source",
            "destination",
            "distance"
        )


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            "id",
            "route",
            "airplane",
            "departure_time",
            "arrival_time",
            "crew",
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "user"
        )


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "row",
            "seat",
            "flight",
            "order",
        )

    def validate(self, data):
        flight = data.get("flight")
        row = data.get("row")
        seat = data.get("seat")

        ticket_exists = Ticket.objects.filter(
            flight=flight,
            row=row,
            seat=seat,
        ).exists()

        if ticket_exists:
            raise serializers.ValidationError(
                "This ticket is busy"
            )

        if row > flight.airplane.rows:
            raise serializers.ValidationError(
                "Row limit exceeded"
            )
        if seat > flight.airplane.seats_in_row:
            raise serializers.ValidationError(
                "Seat limit exceeded"
            )

        return data
