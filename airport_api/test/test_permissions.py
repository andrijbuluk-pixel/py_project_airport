from rest_framework.test import APIClient
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from airport_api.models import Airport, Route, Flight, Airplane, AirplaneType, Crew, Ticket, Order


class PermissionTestNonAuthenticatedUser(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_non_authenticated_user_crew_post(self):
        response = self.client.post(reverse(
            "airport_api:crew-list"),
            data={
                "first_name": "John",
                "last_name": "Doe",
            }
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_authenticated_user_airplanetype_post(self):
        response = self.client.post(reverse(
            "airport_api:type-list"),
            data={
                "name": "AirplaneType",
            }
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_authenticated_user_airplane_post(self):
        airplane_type = AirplaneType.objects.create(name="AirplaneType")

        response = self.client.post(reverse(
            "airport_api:airplane-list"),
            data={
                "name": "Airplane",
                "rows": 20,
                "seats_in_row": 4,
                "airplane_type": airplane_type.id,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_authenticated_user_airport_post(self):
        response = self.client.post(reverse(
            "airport_api:airport-list"),
            data={
                "name": "Airport",
                "closest_big_city": "City",
            }
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_authenticated_user_route_post(self):
        source = Airport.objects.create(
            name="Source",
            closest_big_city="City1"
        )

        destination = Airport.objects.create(
            name="Destination",
            closest_big_city="City2"
        )

        response = self.client.post(reverse(
            "airport_api:route-list"),
            data={
                "source": source.id,
                "destination": destination.id,
                "distance": 500
            }
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_authenticated_user_flight_post(self):
        route = Route.objects.create(
            source=Airport.objects.create(
                name="Source",
                closest_big_city="City1"
            ),
            destination=Airport.objects.create(
                name="Destination",
                closest_big_city="City2"
            ),
            distance=500

        )

        airplane = Airplane.objects.create(
            name="Airplane",
            rows=20,
            seats_in_row=4,
            airplane_type=AirplaneType.objects.create(name="AirplaneType"),
        )

        crew = Crew.objects.create(
            first_name="John",
            last_name="Doe",
        )

        response = self.client.post(reverse(
            "airport_api:flight-list"),
            data={
                "route": route.id,
                "airplane": airplane.id,
                "departure_time": (timezone.now() + timedelta(days=2)).isoformat(),
                "arrival_time": (timezone.now() + timedelta(days=2, hours=4)).isoformat(),
                "crew": [crew.id]
            }
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_non_authenticated_user_order_post(self):
        response = self.client.post(reverse(
            "airport_api:order-list"),
            data={
            }
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PermissionTestAuthenticatedUser(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="john",
            email="john@gmail.com",
            password="testpass"
        )
        self.client.force_authenticate(self.user)

        self.crew = Crew.objects.create(
            first_name="John",
            last_name="Doe",
        )

        self.type = AirplaneType.objects.create(name="AirplaneType")

        self.airplane = Airplane.objects.create(
            name="Airplane",
            rows=20,
            seats_in_row=4,
            airplane_type=self.type
        )

        self.airport1 = Airport.objects.create(
            name="Airport_Test",
            closest_big_city="City_Test",
        )

        self.airport2 = Airport.objects.create(
            name="Test_Airport",
            closest_big_city="Test_City",
        )

        self.route = Route.objects.create(
            source=self.airport1,
            destination=self.airport2,
            distance=500
        )

        self.flight = Flight.objects.create(
            route=self.route,
            airplane=self.airplane,
            departure_time=(timezone.now() + timedelta(days=2)).isoformat(),
            arrival_time=(timezone.now() + timedelta(days=2, hours=4)).isoformat(),
        )
        self.flight.crew.add(self.crew)

        self.order = Order.objects.create(
            user=self.user,
        )

    def test_authenticated_user_crew(self):
        response_get = self.client.get(reverse("airport_api:crew-list"))
        response_post = self.client.post(reverse(
            "airport_api:crew-list"),
            data={
                "first_name": "Test",
                "last_name": "Crew",
            }
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_airplanetype(self):
        response_get = self.client.get(reverse("airport_api:type-list"))
        response_post = self.client.post(reverse(
            "airport_api:type-list"),
            data={
                "name": "AirplaneType",
            }
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_airplane(self):
        response_get = self.client.get(reverse("airport_api:airplane-list"))
        response_post = self.client.post(reverse(
            "airport_api:airplane-list"),
            data={
                "name": "Airplane",
                "rows": 20,
                "seats_in_row": 4,
                "airplane_type": self.airplane.pk
            }
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_airport(self):
        response_get = self.client.get(reverse("airport_api:airport-list"))
        response_post = self.client.post(reverse(
            "airport_api:airport-list"),
            data={
                "name": "Airport",
                "closest_big_city": "City"
            }
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_route(self):
        response_get = self.client.get(reverse("airport_api:route-list"))
        response_post = self.client.post(reverse(
            "airport_api:route-list"),
            data={
                "source": self.airport1.pk,
                "destination": self.airport2.pk,
                "distance": 500,
            }
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_flight(self):
        response_get = self.client.get(reverse("airport_api:flight-list"))
        response_post = self.client.post(reverse(
            "airport_api:flight-list"),
            data={
                "route": self.route.pk,
                "airplane": self.airplane.pk,
                "departure_time": (timezone.now() + timedelta(days=2)).isoformat(),
                "arrival_time": (timezone.now() + timedelta(days=2, hours=4)).isoformat(),
                "crew": [self.crew.pk],
            }
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_order(self):
        response_get = self.client.get(reverse("airport_api:order-list"))
        response_post = self.client.post(reverse(
            "airport_api:order-list"),
            data={
                "user": self.user.pk,
            }
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

    def test_authenticated_user_ticket(self):
        response_get = self.client.get(reverse("airport_api:ticket-list"))
        response_post = self.client.post(reverse(
            "airport_api:ticket-list"),
            data={
                "row": 10,
                "seat": 4,
                "flight": self.flight.pk,
                "order": self.order.pk
            }
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)
