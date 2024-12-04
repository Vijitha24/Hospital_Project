from django.urls import path
from . import views


app_name = 'hospital_admin'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('hospital_admins/', views.hospital_admin_list, name='hospital_admin_list'),
    path('hospital_admins/create/', views.profile, name='create_hospital_admin'),
    path('articles/', views.article_list, name='article_list'),  # URL to list all articles
    path('add-article/', views.add_article, name='add_article'),  # URL to add a new artic
]
