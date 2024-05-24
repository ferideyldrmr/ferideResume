from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AbstractModel(models.Model):
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

    class Meta:
        abstract = True


# Create your models here.
class GeneralSetting(AbstractModel):
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

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the settings.'
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)


class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
    )
    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Location',
    )
    job_description = models.CharField(
        blank=True,
        default='',
        max_length=254,
        verbose_name='Job Description'
    )

    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('-start_date',)

# class ImageSetting(AbstractModel):
#     name = models.CharField(
#         default='',
#         max_length=254,
#         blank=True,
#         verbose_name='Name',
#         help_text='This is variable of the settings.'
#     )
#     description = models.CharField(
#         blank=True,
#         default='',
#         max_length=254,
#         verbose_name='Description'
#     )
#     file = models.ImageField(
#         default='',
#         verbose_name='Image',
#         help_text='',
#         blank=True,
#         upload_to='images/',
#     )
