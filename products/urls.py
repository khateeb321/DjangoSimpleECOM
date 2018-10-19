from django.conf.urls import url, include
from .views import all_products
from products import views

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^emp$', views.emp),
    url(r'^show$', views.show),
    url(r'^edit/<int:id>$', views.edit),
    url(r'^update/<int:id>$', views.update),
    url(r'^delete/<int:id>$', views.destroy),
    ]