# You must CREATE this file inside your 'salesapp' folder.

from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    # / -> Homepage
    path('', views.homepage_view, name='homepage'),
    # /login/ -> Login Page
    path('login/', views.login_view, name='login'),
    # /about/ -> About Us Page
    path('about/', views.about_view, name='about'),
    # /contact/ -> Contact Us Page
    path('contact/', views.contact_view, name='contact'),
]