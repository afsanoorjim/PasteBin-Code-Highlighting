from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns(
    [
        path("", views.api_root),
        path("snippets/", views.SnippetsList.as_view(), name="snippet-list"),
        path("snippets/<int:pk>/", views.SnippetsDetail.as_view(), name="snippets-detail"),
        path("snippets/<int:pk>/highlight/", views.SnippetHighlight.as_view(), name="snippet-highlight",),
        path("users/", views.UserList.as_view(), name="user-list"),
        path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    ]
)
