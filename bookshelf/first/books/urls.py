from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeBook.as_view(), name='home'),

    path('books/<slug:category_slug>/<slug:subcategory_slug>/', ListBook.as_view(), name='subcategory'),
    path('book/<slug:category_slug>/<slug:subcategory_slug>/<int:book_id>/<slug:book_slug>/', get_onebook, name='onebook'),
    path('add-book/', add_new_book, name='add-book'),

]