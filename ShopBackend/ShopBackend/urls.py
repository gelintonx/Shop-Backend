

from django.contrib import admin
from django.urls import path
from authService import views as authService_views
from products import views as products_views
from payments import views as payments_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',authService_views.register),
    path('login/',authService_views.login),
    path('payment/',payments_views.create_payment),
    path('products/', products_views.get_products),
]
