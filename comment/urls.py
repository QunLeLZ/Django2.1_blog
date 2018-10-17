from django.urls import path
from comment import views


urlpatterns = [
    path('comment/post/<str:post_pk>/', views.post_comment, name='post_comment'),
]