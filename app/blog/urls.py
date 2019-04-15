from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ShowNewsView.as_view(), name='blog-home'),
    path('news/<int:pk>', views.DetailNewsView.as_view(), name='detail-news'),
    path('news/add/', views.CreateNewsView.as_view(), name='add-news'),
    path('contacts/', views.contacts, name='blog-contacts'),
]
