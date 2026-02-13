from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Blog, BlogCategory
from blog.mixins import BlogCategoryMixin
from django.views.generic import View
from blog.models import Comment
from blog.forms import CommentForm
from django.contrib import messages


class BlogListView(BlogCategoryMixin, ListView):
    model = Blog
    template_name='blog/blogs.html'
    context_object_name='blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name='blog/blog.html'
    context_object_name='blog'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = self.object
            comment.save()

            messages.success(
                request,
                "تم إرسال تعليقك بنجاح، نشكرك على اهتمامك."
            )
            return redirect(request.META.get('HTTP_REFERER', '/'))


        context = self.get_context_data()
        context['comment_form'] = CommentForm()
        self.render_to_response(context=context)


