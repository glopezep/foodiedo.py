from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'clients'

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(), name='product_list'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='product_detail'),
    url(r'^categories/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(), name='category_detail'),
    url(r'^statuses/$', views.StatusList.as_view(), name='status_list'),
    url(r'^status/(?P<pk>[0-9]+)/$', views.StatusDetail.as_view(), name='status_detail'),
    url(r'^orders/$', views.OrderList.as_view(), name='order_list'),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view(), name='order_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
