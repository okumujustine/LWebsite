from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import  ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    lead_text = models.CharField(
        max_length=140,
        blank=True,
        help_text="Subheading text on the banner"
        )

    button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        help_text="Select an optional page to link to",
        on_delete=models.SET_NULL,
    )

    button_text = models.CharField(
        max_length=50,
        blank=False,
        default="Read More",
        help_text="Button text"
    )

    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank= False,
        null=True,
        related_name="+",
        help_text="The banner background image",
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('lead_text'),
        PageChooserPanel('button'),
        FieldPanel('button_text'),
        ImageChooserPanel('banner_background_image')
    ]
