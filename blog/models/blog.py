from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils.text import slugify

from .base import SiteComponent, Message


class BlogEntry(SiteComponent):
    """The base for content pages within the blog application."""
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_author',
        editable=False,
    )

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_editor',
    )

    topic = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )

    @property
    def author(self):
        return self.created_by.get_full_name()

    @property
    def slug(self):
        return slugify(self.name)

    def get_absolute_url(self):
        return f"/blog/{self.pk}"


class BlogContent(SiteComponent):
    """Special content in a particular section of the blog entry, e.g. images or code."""
    CONTENT_TYPES = [
        ('image', 'image'),
        ('code', 'code'),
        ('text', 'text'),
    ]

    content_type = models.CharField(
        max_length=100,
        choices=CONTENT_TYPES,
    )

    content_text = models.TextField(
        max_length=8000,
        null=True,
        blank=True,
    )

    image_file = models.ImageField(
        upload_to='blog/img/uploads',
        null=True,
        blank=True,
    )


class BlogSection(SiteComponent):
    """Allow blog entries to be broken into separate sections for easy organization + control."""

    order = models.IntegerField(
        verbose_name="ordering of sections within a blog",
        validators=[
            MinValueValidator(0, message="Order must be greater than or equal to zero."),
        ]
    )

    blog = models.ForeignKey(
        BlogEntry,
        on_delete=models.CASCADE,
    )

    content = models.OneToOneField(
        BlogContent,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ['blog', 'order']
        ordering = ['order']


class BlogComment(Message):
    """Comments on blog entries."""
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_commenter',
    )

    blog = models.ForeignKey(
        BlogEntry,
        on_delete=models.CASCADE,
    )
