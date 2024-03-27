from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_customer, name='create-customer'),
    # path('createinfo/', views.create_customer_info, name='create-customer-info'),
    path('list/', views.list_customers, name='list-customers'),
    path('<int:pk>/', views.customer_detail, name='customer-detail'),
    path('<int:pk>/renew/', views.renew_customer_plan, name='renew-customer-plan'),
    path('<int:pk>/upgrade-downgrade/', views.upgrade_downgrade_customer_plan, name='upgrade-downgrade-customer-plan'),

]
