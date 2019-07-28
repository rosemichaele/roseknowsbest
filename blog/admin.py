from django.contrib import admin

from blog.models import Application, Module, BlogEntry, BlogSection, BlogContent


@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):

    exclude = [
        'modified_by',
    ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Application, Module, BlogSection, BlogContent)
class BlogAdmin(admin.ModelAdmin):
    pass

