from django.db import models
from django.utils.text import slugify


class SiteComponent(models.Model):
    """
    Each piece of the website should have certain default attributes that allow it to be identified, controlled, and
    understood. Add an active flag, a name, a description (optional), and created + modified dates to this abstract
    model for other objects to extend.
    """
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=4000,
                                   null=True,
                                   )
    created_date = models.DateTimeField(auto_now_add=True,
                                        editable=False,
                                        )
    modified_date = models.DateTimeField(auto_now=True,
                                         editable=False,
                                         )

    class Meta:
        abstract = True
        ordering = ['created_date']

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class Message(SiteComponent):
    """Abstract model for comments and other simple posts."""
    subject = models.CharField(max_length=200,
                               verbose_name="message subject")
    message_text = models.TextField(max_length=1000,
                                    null=True,
                                    )

    class Meta:
        abstract = True

    def __str__(self):
        return "Message: " + str(self.message_text)


class Application(SiteComponent):
    """
    Distinct applications that will exist on the site, e.g. blog, store, projects, or personal. Links to these will
    exist on the top navigation pane.
    """
    @property
    def url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        return '/' + slugify(self.name)


class Module(SiteComponent):
    """Sub-sections within an application."""
    application = models.ForeignKey(Application,
                                    on_delete=models.CASCADE,
                                    )
