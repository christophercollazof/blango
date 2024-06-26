from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
]
