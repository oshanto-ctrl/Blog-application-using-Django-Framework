from django.urls import path
from .views import (
    BlogPostListView, # List view of posts on page
    BlogPostDetailView, # Detail view of individual post
    BlogPostCreateView, # Create a Blogpost with form
    BlogPostUpdateView, # Update a Blogpost with form
    BlogPostDeleteView, # Delete a BlogPost with form
) 

urlpatterns = [

    path('blogpost/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post_delete'),

    path('blogpost/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='post_edit'),

    path('blogpost/new/', BlogPostCreateView.as_view(), name='post_new'),

    path('blogpost/<int:pk>/', BlogPostDetailView.as_view(),
        name='post_detail'),
    
    path('', BlogPostListView.as_view(), name='home'),
]
