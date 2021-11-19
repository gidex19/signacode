from django.urls import path
from . import views as my_app_view

urlpatterns = [
    path('', my_app_view.home, name = 'homepage'),
    path('login/', my_app_view.loginpage, name='login'),
    path('signup/', my_app_view.signup, name='signup'),
    path('profile/', my_app_view.profile, name='profile'),
    path('services/', my_app_view.services, name='services'),
    path('technews/', my_app_view.technews, name='technews'),
    path('logout/', my_app_view.logout_view, name = 'logout'),
    path('post/<int:pk>/', my_app_view.post_detail , name = 'post-detail'),
    path('technews-detail/<int:pk>/', my_app_view.technews_detail , name = 'technews-detail'),
    ]