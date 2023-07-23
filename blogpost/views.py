from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy
from .models import Post

# BlogPostListView view 
class BlogPostListView(ListView):
    model = Post
    template_name = 'home.html'

# BlogPostDetailView view
class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# BlogPostCreateView view
class BlogPostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

# BlogPostUpdateView view
class BlogPostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

# BlogPostDeleteView view
class BlogPostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')