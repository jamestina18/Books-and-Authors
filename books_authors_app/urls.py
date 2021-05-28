from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-book', views.add_book),
    path('add-book/<int:book_id>', views.display_book),
    path('assign-author/<int:author_id>/assign', views.assign_book),
]
