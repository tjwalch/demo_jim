from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _
import model_utils


class Car(models.Model):
    name = models.CharField(
        _('Namn'),
        max_length=100,
        default='',
        blank=True,
    )
    regno = models.CharField(
        _('Registreringsnummer'),
        max_length=6,
        validators=[validators.RegexValidator(
            r'^[A-Z]{3}[0-9]{3}$',
        )],
    )
    odometer = models.PositiveIntegerField(
        _('Mätarställning'),
        default=0,
    )

    class Meta:
        verbose_name = _('Bil')
        verbose_name_plural = _('Bilar')

    def __str__(self):
        return self.name or self.regno


class TravelLog(models.Model):
    car = models.ForeignKey(
        Car,
        verbose_name=_('Bil'),
        on_delete=models.PROTECT,  # A prod system needs some kind of archiving instead
    )
    date = models.DateField(
        _('Resdatum'),
    )
    mileage_start = models.PositiveIntegerField(
        _('Mätarställning vid start'),
        help_text=_('Mätarställning i km.')
    )
    mileage_end = models.PositiveIntegerField(
        _('Mätarställning vid destination'),
        help_text=_('Mätarställning i km.')
    )
    category = models.CharField(
        _('Kategori'),
        choices=model_utils.Choices(
            ('category_one', _('Kategori ett')),
            ('category_two', _('Kategori två')),
            ('category_three', _('Kategori tre')),
            ('category_four', _('Kategori fyra')),
        ),
        max_length=15,
    )
    participants = models.ManyToManyField(
        'participants.Participant',
        related_name='travelentries',
        verbose_name=_('Deltagare'),
        blank=True,
    )

    class Meta:
        verbose_name = _('Körjournals-post')
        verbose_name_plural = _('Körjournals-poster')

    def __str__(self):
        return '%s %s' % (
            self.car,
            self.date.isoformat()
        )
