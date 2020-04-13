from django.db import models

# Create your models here.

class Coordinate(models.Model):

    id              = models.AutoField(primary_key=True)
    latitude        = models.FloatField(default=0)
    longitude       = models.FloatField(default=0)
    altitude        = models.FloatField(default=0)
    date            = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'Coordinate'
        verbose_name_plural = 'Coordinates'

    def __str__(self):
        return str('{0} : {1} : {2} : {3} : {4}'.format(
            self.id,
            self.latitude,
            self.longitude,
            self.altitude,
            self.date))
