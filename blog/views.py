from django.http import HttpResponse
from django.views import generic

from blog.models import BlogEntry


class SiteIndexView(generic.TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogIndexView(generic.ListView):
    template_name = 'blog/entry-list.html'
    context_object_name = 'blog_entries'

    def get_queryset(self):
        """Return the last five published questions."""
        return BlogEntry.objects.order_by('created_date')


class BlogEntryView(generic.DetailView):
    model = BlogEntry
    template_name = 'blog/entry.html'
