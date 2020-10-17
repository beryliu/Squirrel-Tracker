from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    X = models.FloatField(
        help_text=_('Longitude coordinate'),
    )

    Y = models.FloatField(
        help_text=_('Latitude coordinate'),
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        help_text=_('Unique squirrel id'),
    )

    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = [
        (PM, 'PM'),
        (AM, 'AM'),
    ]
    Shift = models.CharField(
        max_length=15,
        help_text=_('Whether or not the sighting session occurred in the morning or late afternoon'),
        choices=SHIFT_CHOICES,
        blank=True,
    )

    Date = models.DateField(
        help_text=_('Concatenation of the sighting session day and month'),
        blank=True,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    ]
    Age = models.CharField(
        max_length=15,
        help_text=_('Age of squirrel'),
        choices=AGE_CHOICES,
        blank=True,
        null=True,)

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    COLOR_CHOICES = [
        (GRAY, _('Gray')),
        (CINNAMON, _('Cinnamon')),
        (BLACK, _('Black')),
    ]

    Primary_Fur_Color = models.CharField(
        help_text=_('Primary fur color'),
        max_length=15,
        choices=COLOR_CHOICES,
        null=True,
        blank=True,
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = [
        (GROUND_PLANE, _('Ground plane')),
        (ABOVE_GROUND, _('Above ground')),
    ]

    Location = models.CharField(
        help_text=_('Location of where the squirrel was when first sighted'),
        max_length=15,
        choices=LOCATION_CHOICES,
        null=True,
        blank=True,
    )

    Specific_Location = models.CharField(
        max_length=100,
        help_text=_('Specific squirrel location'),
        blank=True,
    )

    Running = models.BooleanField(
        help_text=_('Whether squirrel was seen running'),
    )

    Chasing = models.BooleanField(
         help_text=_('Whether squirrel was seen chasing another squirrel'),
    )

    Climbing = models.BooleanField(
         help_text=_('Whether squirrel was seen climbing a tree or other environmental landmark'),
    )

    Eating = models.BooleanField(
         help_text=_('Whether squirrel was seen eating'),
    )

    Foraging = models.BooleanField(
         help_text=_('Whether squirrel was seen foraging for food'),
    )

    Other_Activities = models.TextField(
        blank=True,
    )

    Kuks = models.BooleanField(
         help_text=_('Whether squirrel was heard kukking'),
    )

    Quaas = models.BooleanField(
         help_text=_('Whether squirrel was heard quaaing'),
    )

    Moans = models.BooleanField(
         help_text=_('Whether squirrel was heard moaning'),
    )

    Tail_flags = models.BooleanField(
         help_text=_('Whether squirrel was seen flagging its tail'),
    )

    Tail_twitches = models.BooleanField(
         help_text=_('Whether squirrel was seen twitching its tail'),
    )

    Approaches = models.BooleanField(
         help_text=_('Whether squirrel was seen approaching human, seeking food'),
    )

    Indifferent = models.BooleanField(
         help_text=_('Whether squirrel was indifferent to human presence'),
    )

    Runs_from = models.BooleanField(
         help_text=_('Whether squirrel was seen running from humans, seeing them as a threat'),
         )

