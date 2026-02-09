from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Blog

class BlogListView(ListView):
    model = Blog
    template_name='blog/blogs.html'
    context_object_name='blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name='blog/blog.html'
    context_object_name='blog'
