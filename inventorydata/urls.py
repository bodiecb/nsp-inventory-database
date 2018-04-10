from django.urls import path

# from django.conf.urls import url

from . import views

app_name = 'inventorydata'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.CheckoutsView.as_view(), name='checkouts'),
    path('<int:item_id>/checkin/', views.checkin, name='checkin'),
    path('<int:item_id>/checkout/', views.checkout, name='checkout'),
    path('item/', views.item, name='item'),
]