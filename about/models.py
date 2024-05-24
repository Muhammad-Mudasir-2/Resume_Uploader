from django.db import models


STATE = {
    'Bwp': 'bwp',
    'Isl': 'Islamabad',
}


class Profile(models.Model):
    name = models.CharField(max_length=100)
    cnic_card = models.IntegerField()
    states = models.CharField(max_length=100, choices=STATE, auto_created=None)
    Date_Time = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100)
    p_images = models.ImageField(upload_to='p_images', blank=True)

