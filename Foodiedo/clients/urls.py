from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'clients'

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(), name='products'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='product'),
    url(r'^categories/$', views.CategoryList.as_view(), name='categories'),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(), name='category'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
