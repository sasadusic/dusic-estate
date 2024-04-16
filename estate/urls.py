"""estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from listings.views import index, list, retrieve, create, update_list, delete_list, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('list/', list, name='list'),
    path('<int:id>/', retrieve, name='retrieve'),
    path('<int:id>/update_list', update_list, name='update_list'),
    path('<int:id>/delete_list', delete_list, name='delete_list'),
    path('create/', create, name='create'),
    # path('<int:pk>/', update_list, name='update'),
    path('about/', about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
