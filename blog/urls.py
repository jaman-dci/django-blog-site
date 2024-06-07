from django.urls import path
from . import views, api_views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('search/', views.post_search, name='post_search'),
    path('create/', views.post_create, name='post_create'),
    # API paths
    path('api/posts/', api_views.PostListCreate.as_view(), name='event-list-create'),
    path('api/posts/<int:pk>/', api_views.PostRetrieveUpdateDestroy.as_view(), name='event-retrieve-update-destroy'),

]



