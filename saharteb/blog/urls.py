from django.urls import path
from blog.views import BlogListView, BlogDetailView

urlpatterns = [

    path("list/", BlogListView.as_view(), name="blog_list"),
    path("<str:slug>/", BlogDetailView.as_view(), name="blog_detail"),
]

