from dateutil.relativedelta import relativedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from model_mommy import mommy

from cars.models import TravelLog
from participants.models import Participant


class TestTravelLogEntry(TestCase):

    def setUp(self):
        self.participants = mommy.make(
            Participant,
            _quantity=5,
        )
        today = timezone.now().date()
        mommy.make(
            TravelLog,
            participants=self.participants[:3],
            mileage_start=100,
            mileage_end=400,
            date=timezone.now().date(),
            _quantity=10,
        )
        self.in_a_month = today + relativedelta(months=1)
        mommy.make(
            TravelLog,
            participants=self.participants[:3],
            mileage_start=100,
            mileage_end=400,
            date=self.in_a_month,
            _quantity=5,
        )

    def test_list_view(self):
        url = reverse('participants-list')
        response = self.client.get(url)
        participants = list(response.context['object_list'])
        self.assertEqual(5, len(participants))
        self.assertEqual(
            1500,
            participants[0].cost(),
        )
        url += '?d=%s' % self.in_a_month.isoformat()
        response = self.client.get(url)
        self.assertEqual(
            750,
            response.context['object_list'][0].cost(),
        )
