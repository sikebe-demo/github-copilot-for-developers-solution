from django.contrib import admin
from django.urls import path
from cats.views import get_cats
from cats.views import insert_cat

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/cats/', get_cats, name='cat-list'),
    path('api/cats/insert/', insert_cat, name='cat-insert'),
]
