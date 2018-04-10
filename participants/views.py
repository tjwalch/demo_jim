from django.db.models import Prefetch, F, Count
from django import forms
from django.utils import timezone
from django.views.generic import ListView

from cars.models import TravelLog
from . import models


class SummaryView(ListView):
    template_name = 'participants/participant_list.html'

    def get_queryset(self):
        try:
            month = forms.DateField().clean(
                self.request.GET.get('d')
            ).month
        except forms.ValidationError:
            month = timezone.now().date().month

        return models.Participant.objects.all().prefetch_related(
            Prefetch(
                'travelentries',
                TravelLog.objects.filter(
                    date__month=month,
                ).annotate(
                    distance=F('mileage_end') - F('mileage_start'),
                    num_participants=Count('participants'),
                ),
                to_attr='annotated_log',
            ),
        )
