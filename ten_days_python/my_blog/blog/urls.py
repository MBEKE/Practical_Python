from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.homepage, name='homepage'),
        path('post/<int:post_id>/', views.post_detail, name='post_detail'),
        path('post/add', views.add_post, name='add_post'),
        path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
        path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
        path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='login')
        ]
