from django.urls import path
from .views import blog_list,blog_detail
app_name ="blogs"

urlpatterns = [
    path('blog/', blog_list, name='blog_list'),  # list of posts
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),  # single post
]

