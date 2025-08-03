from django.urls import path
from snippets.views import UserViewSet, SnippetViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers



snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('users/', user_list, name='user-list'), #type: ignore
    path('users/<int:pk>/', user_detail, name='user-detail'), #type: ignore
    path('snippets/', snippet_list, name='snippet-list'), #type: ignore
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'), #type: ignore
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'), #type: ignore
])

urlpatterns = format_suffix_patterns(urlpatterns)
