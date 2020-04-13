from django.db import models
from signalData.models import Coordinate

# Create your models here.

class User(models.Model):

    id               = models.AutoField(primary_key=True)
    code             = models.CharField(max_length=100, default='xxxxxxxx')
    username         = models.CharField(max_length=100, default='Anonymous')
    password         = models.CharField(max_length=100)
    coordinates      = models.ManyToManyField(Coordinate)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'Uset'
        verbose_name_plural = 'Users'

    def __str__(self):
        return str('{0} : {1}'.format(
            self.id,
            self.username))
