from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page
from wagtail.search import index


class IndexPage(Page):
    landing_text = RichTextField(blank=True)
    landing_picture = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Background landing picture",
    )

    contact_title = models.CharField(max_length=250)
    contact_text = RichTextField(blank=True)
    contact_button = models.CharField(max_length=250)
    contact_address = models.EmailField(max_length=250)

    content_panels = [
        *Page.content_panels,
        MultiFieldPanel(["landing_text", "landing_picture"], heading="Landing content"),
        MultiFieldPanel(
            ["contact_title", "contact_text", "contact_button", "contact_address"], heading="Contact content"
        ),
        "expertise",
        "projects",
    ]

    search_fields = Page.search_fields + [
        index.SearchField("landing_intro"),
        index.SearchField("landing_text"),
        index.SearchField("contact_title"),
        index.SearchField("contact_text"),
        index.SearchField("contact_button"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["projects"] = [item.as_dict() for item in self.projects.all()]
        return context


class Expertise(Orderable):
    page = ParentalKey(IndexPage, on_delete=models.CASCADE, related_name="expertise")
    image = models.ForeignKey("wagtailimages.Image", on_delete=models.CASCADE, related_name="+")
    title = models.CharField(blank=True, max_length=250)
    description = RichTextField(blank=True)

    panels = ["image", "title", "description"]


class Projects(Orderable):
    page = ParentalKey(IndexPage, on_delete=models.CASCADE, related_name="projects")
    image = models.ForeignKey("wagtailimages.Image", on_delete=models.CASCADE, related_name="+")
    caption = models.CharField(blank=True, max_length=250)

    panels = ["image", "caption"]

    def as_dict(self):
        return {
            "title": self.caption,
            "picture": self.image.file.url,
        }


class AboutPage(Page):
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="About banner picture",
    )

    main_text = RichTextField(blank=True)
    main_picture = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Main about picture",
    )

    our_mission_title = models.CharField(max_length=250)
    our_mission_text = RichTextField(blank=True)

    our_activity_title = models.CharField(max_length=250)
    our_activity_text = RichTextField(blank=True)

    education_title = models.CharField(max_length=250)
    education_subtitle = models.CharField(max_length=250)
    education_text = RichTextField(blank=True)

    bottom_text = RichTextField(blank=True)
    bottom_button_label = models.CharField(max_length=250)

    content_panels = [
        *Page.content_panels,
        "banner",
        MultiFieldPanel(["main_text", "main_picture"], heading="Main about content"),
        MultiFieldPanel(["our_mission_title", "our_mission_text", "our_mission_images"], heading="Our mission content"),
        MultiFieldPanel(["our_activity_title", "our_activity_text"], heading="Our activity content"),
        MultiFieldPanel(
            ["education_title", "education_subtitle", "education_text", "education_images"], heading="Education content"
        ),
        MultiFieldPanel(["bottom_text", "bottom_button_label"], heading="Bottom content"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("main_text"),
        index.SearchField("our_mission_title"),
        index.SearchField("our_mission_text"),
        index.SearchField("our_activity_title"),
        index.SearchField("our_activity_text"),
        index.SearchField("education_title"),
        index.SearchField("education_subtitle"),
        index.SearchField("education_text"),
        index.SearchField("bottom_text"),
        index.SearchField("bottom_button_label"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["education_gallery_pictures"] = [image.url for image in self.education_images.all()]
        return context


class OurMissionImages(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name="our_mission_images")
    image = models.ForeignKey("wagtailimages.Image", on_delete=models.CASCADE, related_name="+")
    caption = models.CharField(blank=True, max_length=250)

    panels = ["image", "caption"]


class EducationImages(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name="education_images")
    image = models.ForeignKey("wagtailimages.Image", on_delete=models.CASCADE, related_name="+")
    caption = models.CharField(blank=True, max_length=250)

    panels = ["image", "caption"]

    @property
    def url(self):
        return self.image.file.url


class BlogIndexPage(Page):
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="About banner picture",
    )

    content_panels = [
        *Page.content_panels,
        "banner",
    ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey("BlogPage", related_name="tagged_items", on_delete=models.CASCADE)


class BlogPage(Page):
    date = models.DateField("Post date")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Blog thumbnail image",
    )
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = [
        *Page.content_panels,
        "date",
        MultiFieldPanel(["tags", "image"], heading="Document information"),
        "intro",
        "body",
    ]

    parent_page_types = ["core.BlogIndexPage"]
