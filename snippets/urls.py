from django.urls import path,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('user/', views.User_list),
    path('user/<int:pk>/', views.User_detail),
    path('activity/', views.Activity_list),
    path('activity/<int:pk>/', views.Activity_detail),
    path('rend/', views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


