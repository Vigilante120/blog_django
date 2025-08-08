from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"), #/blog/
    path("/posts", views.posts, name="posts-page"),
    path("/post/<slug:slug>", views.post_detail, name="post-detail-page") #/postsss/my-first-postss these are slug bro keep it in mind
]
