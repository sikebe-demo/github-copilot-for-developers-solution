from django.contrib import admin
from django.urls import path
from cats.views import get_cats, insert_cat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cats/', get_cats, name='get_cats'),
    path('api/insert_cat/', insert_cat, name='insert_cat'),
]