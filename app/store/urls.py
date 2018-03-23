from django.urls import path

from app.store import views

app_name = 'store'

urlpatterns = [
    path('', views.BookList.as_view(), name='list'),
    path('create', views.CreateBook.as_view(), name='create'),
    path('edit/<int:pk>/', views.EditBook.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteBook.as_view(), name='delete'),
]
