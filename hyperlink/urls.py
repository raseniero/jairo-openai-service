from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),

    path('seller/', views.getSellerList, name='sellers'),
    path('seller/<str:pk>/', views.getSellerDetail, name='seller-detail'),
    path('seller-create/', views.sellerCreate, name='seller-create'),
    path('seller-update/<str:pk>/', views.sellerUpdate, name='seller-update'),
    path('seller-delete/<str:pk>/', views.sellerDelete, name='seller-delete'),

    path('buyer/', views.getBuyerList, name='buyers'),
    path('buyer/<str:pk>/', views.getBuyerDetail, name='buyer-detail'),
    path('buyer-create/', views.buyerCreate, name='buyer-create'),
    path('buyer-delete/<str:pk>/', views.buyerDelete, name='buyer-delete'),

    path('company/', views.getCompanyList, name='company'),
    path('company/<str:pk>/', views.getCompanyDetail, name='company-detail'),
    path('company-create/', views.companyCreate, name='company-create'),
    path('company-update/<str:pk>/', views.companyUpdate, name='company-update'),
    path('company-delete/<str:pk>/', views.companyDelete, name='company-delete'),

    path('hyperlink/', views.getHyperlinkList, name='hyperlink'),
    path('hyperlink/<str:pk>/', views.getHyperlinkDetail, name='hyperlink-detail'),
    path('hyperlink-create/', views.hyperlinkCreate, name='hyperlink-create'),
    path('hyperlink-update/<str:pk>/', views.hyperlinkUpdate, name='hyperlink-update'),
    path('hyperlink-delete/<str:pk>/', views.hyperlinkDelete, name='hyperlink-delete'),

    path('access-code/', views.getCodeList, name='access-code'),
    path('access-code/<str:pk>/', views.getCodeDetail, name='access-code-detail'),
    path('access-code-create/', views.codeCreate, name='access-code-create'),
    path('access-code-update/<str:pk>/', views.codeUpdate, name='access-code-update'),
    path('access-code-delete/<str:pk>/', views.codeDelete, name='access-code-delete'),

    path('product/', views.getProductList, name='product'),
    path('product/<str:pk>/', views.getProductDetail, name='product-detail'),
    path('product-create/', views.productCreate, name='product-create'),
    path('product-update/<str:pk>/', views.productUpdate, name='product-update'),
    path('product-delete/<str:pk>/', views.productDelete, name='product-delete'),

    path('cart/', views.getCartList, name='cart'),
    path('cart/<str:pk>/', views.getCartDetail, name='cart-detail'),
    path('cart-create/', views.cartCreate, name='cart-create'),
    path('cart-update/<str:pk>/', views.cartUpdate, name='cart-update'),
    path('cart-delete/<str:pk>/', views.cartDelete, name='cart-delete'),

    path('placed-product/', views.getPlacedProductList, name='placed-product'),
    path('placed-product/<str:pk>/', views.getPlacedProductDetail, name='placed-product-detail'),
    path('placed-product-create/', views.placedProductCreate, name='placed-product-create'),
    path('placed-product-delete/<str:pk>/', views.placedProductDelete, name='placed-product-delete'),

    path('purchased-order/', views.getPurchasedOrderList, name='purchased-order'),
    path('purchased-order/<str:pk>/', views.getPurchasedOrderDetail, name='purchased-order-detail'),
    path('purchased-order-create/', views.purchasedOrderCreate, name='purchased-order-create'),
    path('purchased-order-delete/<str:pk>/', views.purchasedOrderDelete, name='purchased-order-delete'),
]
