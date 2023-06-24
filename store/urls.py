from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('signup/', views.signupPage, name='signUp'),
    path('login/', views.loginPage, name='login'),
    path('home/', views.homePage, name='homepage'),
    path('logout/', views.logoutPage, name='logout'),
    path('search/', views.search, name='search'),
    path('search/<id>', views.searchURL, name='searchurl'),
    path('contact/', views.contact, name='contact'),
    path('preview/<id>', views.preview, name='preview'),
    path('aboutus', views.aboutUs, name='aboutus'),
    path('checkout/', views.checkOut, name='checkout'),
    path('orderTracker/', views.orderTrack, name='ordertracker'),
]
