from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('seller/', views.getSellerList, name='seller'),
    path('seller/<str:pk>/', views.getSellerDetail, name='seller-detail'),
    path('seller-create/', views.sellerCreate, name='seller-create'),
    path('seller-update/<str:pk>/', views.sellerUpdate, name = 'seller-update'),
    path('seller-delete/<str:pk>/', views.sellerDelete, name = 'seller-delete'),
    path('company/', views.getCompanyList, name='company'),
    path('company/<str:pk>/', views.getCompanyDetail, name='company-detail'),
    path('company-create/', views.companyCreate, name='company-create'),
    path('company-update/<str:pk>/', views.companyUpdate, name = 'company-update'),
    path('company-delete/<str:pk>/', views.companyDelete, name = 'company-delete'),
]
