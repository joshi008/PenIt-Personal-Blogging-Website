"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from blog.views import blog_post_create_view

from searches.views import search_view

from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('', home_page),
	
    path('about/', about_page),
	
    path('blog-new/', blog_post_create_view),
    path('blog/', include('blog.urls')),
    path('search/',search_view),

    re_path(r'^prices?/$', about_page),
	path('example/', example_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
