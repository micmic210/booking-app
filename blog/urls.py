from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<int:id>/', views.blog_detail, name='blog_detail'),
    path('<int:id>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('<int:id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]

