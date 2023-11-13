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

    # Test blogpost create view
    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New Title',
            'body': 'New text body',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New Title')
        self.assertEqual(Post.objects.last().body, 'New text body')
    
    # Test post update view
    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated Title',
            'body': 'Updated text body',
        })
        self.assertEqual(response.status_code, 302)
    
    # Test post delete view
    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)




