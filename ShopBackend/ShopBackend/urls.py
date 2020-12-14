

from django.contrib import admin
from django.urls import path
from authService import views as authServiceViews
from products import views as productsViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',authServiceViews.register),
    path('login/',authServiceViews.login),
    path('products/', productsViews.get_products),
]
