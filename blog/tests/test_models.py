from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import BlogEntry, Application


class TestBaseSiteComponent(TestCase):
    def setUp(self):
        self.test_component = Application.objects.create(name='Test App',
                                                         description='Testing base component features.')
        self.test_component.name = 'Updated Test App'
        self.test_component.save()

    def test_components_active_by_default(self):
        self.assertTrue(self.test_component.active)

    def test_created_date_before_modified_date_if_updated(self):
        self.assertLess(self.test_component.created_date,
                        self.test_component.modified_date)


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
        """Blog entry URL slugs are based on the defined name."""
        self.assertEqual(self.entry.slug, 'test-entry')

    def test_absolute_url_from_pk(self):
        self.assertEqual(self.entry.get_absolute_url(), '/blog/' + str(self.entry.pk))


class ApplicationTest(TestCase):
    def setUp(self):
        self.app = Application.objects.create(name='My Great app',
                                              description='Testing the Application model.')

    def test_absolute_url_from_name(self):
        self.assertEqual(self.app.url, '/my-great-app/')
