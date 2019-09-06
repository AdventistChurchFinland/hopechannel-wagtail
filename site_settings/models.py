from django.db import models

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting(icon='mail')
class ContactInformationSettings(BaseSetting):
    """Contact information settings"""

    name = models.CharField(blank=True, null=True, max_length=255)
    address = models.CharField(blank=True, null=True, max_length=255)
    post_code = models.CharField(blank=True, null=True, max_length=10)
    city = models.CharField(blank=True, null=True, max_length=255)
    phone = models.CharField(blank=True, null=True, max_length=50)

    panels = [
        FieldPanel('name'),
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('post_code'),
            FieldPanel('city'),
        ], heading="Address"),
        MultiFieldPanel([
            FieldPanel('phone'),
        ], heading="Phone")
    ]

    class Meta:
        verbose_name = 'Contact Information'
