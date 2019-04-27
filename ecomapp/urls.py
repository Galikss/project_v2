from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.base_view, name='base'),
    re_path(r'^product/(?P<product_slug>[-\w]+)/$', views.product_view, name='product_detail'),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', views.category_view, name='category_detail'),
]


