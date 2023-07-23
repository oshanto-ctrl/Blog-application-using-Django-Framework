from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Import Model
from .models import Post

# BlogPostTest Class
class BlogPostTest(TestCase):

    # Set up test user and post
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpass',
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice Body Content',
            author=self.user,
        )
    # Test string representation
    def test_string_representation(self):
        post = Post(title='A good title')
        self.assertEqual(str(post), post.title)

    # Test post contents
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice Body Content')
    
    # Test blogpost list view
    def test_blogpost_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice Body Content')
        self.assertTemplateUsed(response, 'home.html')
    
    # Test blogpost detail view
    def test_blogpost_detail_view(self):
        response = self.client.get('/blogpost/1/')
        no_response = self.client.get('/blogpost/100/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    




