from django.urls import path, re_path
from blog.views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path("list/", BlogListView.as_view(), name="blog_list"),
    re_path(r'^(?P<slug>[-\w\u0600-\u06FF]+)/$', BlogDetailView.as_view(), name='blog_detail')
]

