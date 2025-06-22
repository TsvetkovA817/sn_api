"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as auth_views
from posts import views as posts_views


urlpatterns = [
      path('admin/', admin.site.urls),

      # API 
      path('api/posts/', posts_views.PostListCreateView.as_view(), name='post-list-create'),
      path('api/posts/<int:pk>/', posts_views.PostDetailView.as_view(), name='post-detail'),
      path('api/posts/<int:post_id>/comments/', posts_views.CommentCreateView.as_view(),
           name='comment-create'),
      path('api/posts/<int:post_id>/like/', posts_views.LikePostView.as_view(), name='like-post'),

      # авторизация
      path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
      path('api/auth-token/', auth_views.obtain_auth_token, name='get-auth-token'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


