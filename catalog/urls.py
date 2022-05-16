from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),

    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailViews.as_view(), name='book-detail'),

    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrower'),
    
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]

# Примечание: В качестве дополнительного задания, рассмотрите возможность того, как вы могли бы закодировать url на список всех книг, вышедших в определённый год, месяц, день и какое РВ (паттерн) должно соответствовать этому.
