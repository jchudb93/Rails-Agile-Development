
from django.conf.urls import url

from products.views import (
 ProductListView,
 # product_list_view, 
 #ProductDetailView,
 ProductDetailSlugView, 
 #product_detail_view,
 #ProductFeaturedListView,
 #ProductFeaturedDetailView
 )


urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
   #  url(r'^featured/$', ProductFeaturedListView.as_view()),
   #  url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),


]