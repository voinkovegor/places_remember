
from django.contrib.auth.models import AbstractUser

from django.contrib.gis.db import models
from django.urls import reverse_lazy
from django.utils import timezone

from geodjango import settings

from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


    class Meta:
        ordering = ['name']


class User(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    avatar = models.CharField(max_length=255, null=True, blank=True)



class Memory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    location = models.PointField(verbose_name='Координаты')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User', on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    def get_absolute_url(self):
        return reverse_lazy('detail_memory', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title





class Migration(migrations.Migration):
    operations = [
        CreateExtension('postgis'),
    ]