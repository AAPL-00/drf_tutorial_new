from django.urls import path
from snippets import views


urlpatterns = [
    path('snippets/', views.snippet_list), #type: ignore
    path('snippets/<int:pk>/', views.snippet_detail), #type: ignore
]
