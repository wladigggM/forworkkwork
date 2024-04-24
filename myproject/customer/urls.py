from django.urls import path

from customer.views import CustomerDashboard, Index

app_name = 'customer'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('customer/', CustomerDashboard.as_view(), name='customer'),

]
