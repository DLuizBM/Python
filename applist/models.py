from django.db import models


class Reservation(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20, default='#')
    reservation_date = models.CharField('Reservation date', max_length=10, default='#', help_text='Ex: 01/01/2020')
    hour = models.CharField(verbose_name='Reservation time', max_length=5, default='#', help_text="Ex: 20:00")
    people = models.CharField(verbose_name='Table for?', max_length=3, default='#', help_text="Ex: 30")
    date_made = models.DateField(verbose_name='Creantion date and time', auto_now_add=True, null=True)
    observations = models.TextField(verbose_name='Observations', max_length=500, blank=True)


    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.name
