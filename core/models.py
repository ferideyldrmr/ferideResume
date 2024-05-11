from django.db import models


# Create your models here.
class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the settings.'
    )
    description = models.CharField(
        blank=True,
        default='',
        max_length=254,
        verbose_name='Description'
    )
    parameter = models.CharField(
        blank=True,
        max_length=254,
        default='',
        verbose_name='Parameter'
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated date'
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created date'
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)
