from django.urls import path
from blog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('archives/<str:year>/<str:month>/', views.archives, name='archives'),
    path('category/<int:id>', views.search_category, name='category_menu'),
    path('tag/<str:tag>', views.search_tag, name='search_tag'),
    path('about', views.about_me, name='about_me'),
]