from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.access_entry, name="access_entry"),
    path('create/', views.create_page, name='create'),
    path('random/', views.random_page, name="random"),
    path('search/', views.search_page, name='search'),
    path('edit/<str:title>', views.edit_page, name='edit')
]
