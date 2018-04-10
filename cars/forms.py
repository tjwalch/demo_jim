from django import forms
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from . import models


class TravelLogForm(forms.ModelForm):

    class Meta:
        model = models.TravelLog
        fields = (
            'car',
            'date',
            'mileage_start',
            'mileage_end',
            'category',
            'participants',
        )

    class Media:
        js = (
            'admin/js/vendor/jquery/jquery.js',
            reverse_lazy('js_reverse'),
            'cars/travelentry.js',
        )

    def clean_participants(self):
        participants = self.cleaned_data.get('participants', [])
        if len(participants) > 4:
            raise forms.ValidationError(
                _('Max antal deltagare är 4.'),
            )
        return participants

    def clean(self):
        errors = {}
        mileage_start = self.cleaned_data.get('mileage_start', 0)
        car = self.cleaned_data.get('car')
        # Validate that start mileage isn't lower than car odometer
        if (car and mileage_start) and (mileage_start < car.odometer):
            errors['mileage_start'] = _('Mätarställning vid start '
                                        'kan inte vara lägre än bilens.')

        # Validate that destination mileage > start
        if mileage_start > self.cleaned_data.get('mileage_end', 0):
            errors['mileage_end'] = _('Mätarställning vid destination '
                                      'kan inte vara mindre än vid start.')

        if errors:
            raise forms.ValidationError(errors)

        return self.cleaned_data
