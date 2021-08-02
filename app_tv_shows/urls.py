from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.shows),
    path('shows/new', views.create_page),
    path('shows/<int:id>', views.display_page),
    path('shows/<int:id>/edit', views.edit_page),
    path('shows/create', views.create_new),
    path('shows/<int:id>/update', views.update_show),
    path('shows/<int:id>/destroy', views.delete_show)
]