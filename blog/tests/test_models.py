from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import BlogEntry


class BlogEntryTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='blog_tester',
                                             email='blog_tester@test.roseknowsbest.com',
                                             password='top_secret',
                                             first_name='Blog',
                                             last_name='Tester')
        self.entry = BlogEntry.objects.create(name='Test Entry',
                                              description='This a test entry.',
                                              created_by=self.user,
                                              modified_by=self.user)

    def test_blog_entry_has_author(self):
        """Blog entries are automatically authored by the user who creates them."""
        self.assertEqual(self.entry.author, 'Blog Tester')

    def test_blog_entry_name_slug(self):
        """Blog entry URL slugs are based of the defined name."""
        self.assertEqual(self.entry.slug, 'test-entry')
