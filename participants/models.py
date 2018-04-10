from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Participant(models.Model):
    first_name = models.CharField(
        _('Förnamn'),
        max_length=100,
    )
    last_name = models.CharField(
        _('Efternamn'),
        max_length=100,
    )

    class Meta:
        verbose_name = _('Deltagare')
        verbose_name_plural = _('Deltagare')

    def __str__(self):
        return '%s %s' % (
            self.first_name,
            self.last_name,
        )

    def cost(self):
        price_km = settings.SEK_10KM / 10
        return sum(
            (e.distance * price_km) / e.num_participants for e in self.annotated_log
        )
