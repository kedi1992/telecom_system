from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_plan, name='create-plan'),
    path('list/', views.list_plans, name='list-plans'),
    # path('<int:pk>/', views.plan_detail, name='plan-detail'),
]
