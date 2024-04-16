from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('<int:id>/', views.retrieve, name='retrieve'),
    path('<int:id>/update_list', views.update_list, name='update_list'),
    path('<int:id>/delete_list', views.delete_list, name='delete_list'),
    path('create/', views.create, name='create'),
    # path('<int:pk>/', update_list, name='update'),

    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
]