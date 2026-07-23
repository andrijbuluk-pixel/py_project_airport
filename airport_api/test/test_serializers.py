from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from django.test import TestCase

from airport_api.models import Airport, Route, Flight, Airplane, AirplaneType, Crew, Ticket, Order


AIROPORT_URL = reverse("airport_api:ticket-list")


class TickerSerializer(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "admin@admin.com", "testpass", is_staff=True
        )
        self.client.force_authenticate(self.user)


        self.airplane_type = AirplaneType.objects.create(
            name="AirplaneType"
        )

        self.crew1 = Crew.objects.create(
            first_name="FirstName",
            last_name="LastName",
        )
        self.crew2 = Crew.objects.create(
            first_name="TestName",
            last_name="TestLastName",
        )

        self.airport_prague = Airport.objects.create(
            name="Prague Airport",
            closest_big_city="Prague"
        )
        self.airport_berlin = Airport.objects.create(
            name="Berlin Airport",
            closest_big_city="Berlin"
        )

        self.route = Route.objects.create(
            source=self.airport_prague,
            destination=self.airport_berlin,
            distance=800
        )

        self.airplane = Airplane.objects.create(
            name="Airplane",
            rows=20,
            seats_in_row=4,
            airplane_type=self.airplane_type,
        )

        now = timezone.now()
        self.flight = Flight.objects.create(

            route=self.route,
            airplane=self.airplane,
            departure_time=(now + timedelta(days=2)).isoformat(),
            arrival_time=(now + timedelta(days=2, hours=4)).isoformat(),
        )
        self.flight.crew.set([self.crew1, self.crew2])

        self.order = Order.objects.create(
            user=self.user,
        )

    def test_create_ticket(self):
        data = {
            "row": 3,
            "seat": 2,
            "flight": self.flight.id,
            "order": self.order.id,
        }

        response = self.client.post(AIROPORT_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
