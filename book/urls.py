from django.urls import path
from book import views

app_name = 'book'
urlpatterns = [
    # 書籍
    path('', views.book_list, name='book_list'),   # 一覧
    path('add/', views.book_edit, name='book_add'),  # 登録
    path('mod/<int:book_id>/', views.book_edit, name='book_mod'),  # 修正
    path('del/<int:book_id>/', views.book_del, name='book_del'),   # 削除
]
