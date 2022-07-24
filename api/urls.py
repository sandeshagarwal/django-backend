from django.urls import path
from . import views

urlpatterns = [
    #path('',views.apiOverview,name="api-overview"),
    path('sales/list/',views.carSalesList,name="sales-list"),
    path('sales/detailbyid/<str:pk>/',views.carDetailsbysales_id,name="sales-detail-by-sales_id"),
    path('sales/detailcustomer/<str:pk>/',views.carDetailsbycustomer_id,name="sales-detail-by-customer_id"),
    path('sales/create/',views.carSalesCreate,name="sales-create"),
    path('sales/update/<str:pk>/',views.carSalesUpdate,name="sales-update"),
    path('sales/delete/<str:pk>/',views.carSalesDelete,name="sales-delete"),
]