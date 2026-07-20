from django.conf import settings
from django.db import models


class Crew(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AirplaneType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Type - {self.name}"


class Airplane(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    airplane_type = models.ForeignKey(
        AirplaneType,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Airplane - {self.name}"


class Airport(models.Model):
    name = models.CharField(max_length=200)
    closest_big_city = models.CharField(max_length=200)

    def __str__(self):
        return f"Airport - {self.name}"


class Route(models.Model):
    source = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="route_source",
    )
    destination = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="route_destination",
    )
    distance = models.IntegerField()

    def __str__(self):
        return f"Route - {self.source} -> {self.destination} | {self.distance}"


class Flight(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    crew = models.ManyToManyField(Crew)

    def __str__(self):
        return f"{self.route}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Order - {self.user} | {self.created_at}"


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket - {self.row} | {self.seat} | {self.flight}"
