from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('users/', views.UserList.as_view()), #type: ignore
    path('users/<int:pk>/', views.UserDetail.as_view()), #type: ignore
    path('snippets/', views.SnippetList.as_view()), #type: ignore
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()), #type: ignore
]

urlpatterns = format_suffix_patterns(urlpatterns)
