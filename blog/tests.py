from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from .models import Post
from django.utils import timezone

from . import views

# Create your tests here.
class PostTests(TestCase):
    def setUp(self):
        self.post = Post()
        self.post.author = "BBC"
        self.post.title = "China hacks into million database"
        self.post.content = "A ver long text about china."
        self.post.created_date = timezone.now()
        self.post.views = 0
        self.post.save()

    def test_post_fields(self):
        postedpost = Post.objects.get(pk=self.post.id)
        self.assertEqual(postedpost, self.post)

    def test_newsitems_page_status_code(self):
        response = self.client.get('/posts/')
        self.assertEquals(response.status_code, 200)

    def test_newsdetails_page_status_code(self):
        response = self.client.get('/posts/1/')
        self.assertEquals(response.status_code, 200)

    def test_newsform_page_status_code(self):
        response = self.client.get('/posts/new/')
        self.assertEquals(response.status_code, 302)