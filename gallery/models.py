from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.core.models import Orderable, Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import  ImageChooserPanel
from wagtail.snippets.edit_handlers import  SnippetChooserPanel
from wagtail.snippets.models import register_snippet

# Create your models here.

class GalleryImageOrderable(Orderable):
    "allows us to select one or more gallery images from snippets"

    page = ParentalKey('gallery.GalleryPage', related_name="gallery_image_orderable")
    
    image = models.ForeignKey(
        'gallery.GalleryImage',
        on_delete=models.CASCADE,
    )

    panels = [
        SnippetChooserPanel('image')
    ]


@register_snippet
class GalleryImage(models.Model):
    """ Gallery image snippets """

    title = models.CharField(max_length=255)

    image = models.ForeignKey(
        'wagtailimages.Image',
        blank= False,
        null=True,
        related_name="+",
        help_text="Gallery image",
        on_delete=models.SET_NULL,
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('title'),
                ImageChooserPanel('image'),
            ],
            heading = "Title and image"
        )
    ]

    def __str__(self):
        return self.title


class GalleryListingPage(Page):

    template = 'gallery/gallery_listing_page.html'

    subtitle = models.CharField(
        max_length=250,
        blank=True
        )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['galleries'] = GalleryPage.objects.all().live().public()
        return context


class GalleryPage(Page):

    template = 'gallery/gallery_page.html'

    description = models.CharField(max_length=250)

    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    gallery_image = models.ForeignKey(
        'wagtailimages.Image',
        blank= True,
        null=True,
        related_name="+",
        help_text="It will be used in the gallery listing page",
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        PageChooserPanel('internal_page'),
        MultiFieldPanel(
            [
                InlinePanel('gallery_image_orderable', label="image select", min_num=1, max_num=50),
                
            ],
            heading="Select Images"
        ),
        ImageChooserPanel('gallery_image')
    ]

