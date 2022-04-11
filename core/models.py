import math
from django.db import models
from django.utils.translation import gettext_lazy as _


class Airplane(models.Model):
    airplane_id = models.BigIntegerField(_('Airplane ID'), primary_key=True)
    airplane_name = models.CharField(_('Airplane name'), max_length=100, blank=False)
    passengers_count = models.PositiveIntegerField(_('Passengers count'), blank=False)

    def __str__(self):
        return f"{self.airplane_name} - {self.airplane_id}"

    @property
    def capacity(self) -> int:
        return 200 * self.airplane_id

    @property
    def fuel_consumption_per_min(self) -> float:
        return round((math.log(self.airplane_id) * 0.08) + (self.passengers_count * 0.002), 3)

    @property
    def max_minutes_able_to_fly(self) -> int:
        return round(self.capacity / self.fuel_consumption_per_min)
