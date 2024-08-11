from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('snippets/', views.SnippetsList.as_view()),
    path('snippets/<int:pk>/', views.SnippetsDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)