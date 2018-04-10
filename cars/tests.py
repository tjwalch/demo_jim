from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from model_mommy import mommy

from cars.models import Car, TravelLog
from participants.models import Participant


class TestTravelLogEntry(TestCase):

    def setUp(self):
        self.participants = mommy.make(
            Participant,
            _quantity=5,
        )
        self.car = mommy.make(
            Car,
            odometer=100,
        )
        self.form_url = reverse('travelentry')
        self.data = {
            'car': self.car.pk,
            'mileage_start': 150,
            'mileage_end': 200,
            'category': 'category_one',
            'date': timezone.now().date().isoformat(),
            'participants': [
                self.participants[0].pk,
                self.participants[1].pk,
            ]
        }

    def test_add_entry(self):
        response = self.client.post(self.form_url, self.data)
        self.assertRedirects(response, self.form_url)
        self.assertEqual(1, TravelLog.objects.count())

    def test_max_participants(self):
        self.data['participants'] = [p.pk for p in self.participants]
        response = self.client.post(self.form_url, self.data)
        self.assertFormError(
            response, 'form', 'participants',
            'Max antal deltagare är 4.',
        )

    def test_destination_after_start(self):
        self.data['mileage_start'] = 300
        response = self.client.post(self.form_url, self.data)
        self.assertFormError(
            response, 'form', 'mileage_end',
            'Mätarställning vid destination '
            'kan inte vara mindre än vid start.'
        )

    def test_start_less_than_odometer(self):
        self.data['mileage_start'] = 80
        response = self.client.post(self.form_url, self.data)
        self.assertFormError(
            response, 'form', 'mileage_start',
            'Mätarställning vid start '
            'kan inte vara lägre än bilens.'
        )

    def test_odometer_view(self):
        url = reverse('retreive-odometer', args=(self.car.pk, ))
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertEqual(100, data['odometer'])
