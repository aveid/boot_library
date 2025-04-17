from django.urls import path
from . import views

urlpatterns = [
    # path('authors/', views.AuthorAPIView.as_view(), name='authors')
    path('authors/', views.get_all_authors, name='authors'),
    path('authors/<int:pk>/', views.get_author, name='author_detail'),

]