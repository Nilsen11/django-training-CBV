from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ShowNewsView.as_view(), name='blog-home'),
    path('news/<int:pk>', views.DetailNewsView.as_view(), name='detail-news'),
    path('news/add/', views.CreateNewsView.as_view(), name='add-news'),
    path('news/<int:pk>/update/', views.UpdateNewsView.as_view(), name='update-news'),
    path('contacts/', views.contacts, name='blog-contacts'),
]
