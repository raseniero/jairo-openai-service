from django.shortcuts import render
from .models import Seller, Company
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import SellerSerializer, CompanySerializer
from rest_framework import status


#API ROOT
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Sellers' : 'http://127.0.0.1:8000/hyperlink/seller/',
        'Seller Detail View' : '/seller/<str:pk>/',
        'Create Seller' : '/seller-create',
        'Update Seller' : '/seller-update/<str:pk>/',
        'Delete Seller' : '/seller-delete/<str:pk>/',

        'Companies' : '/company',
        'Company Detail View' : '/company/<str:pk>/',
        'Create Company' : '/company-create',
        'Update Company' : '/company-update/<str:pk>/',
        'Delete Company' : '/company-delete/<str:pk>/',
    }
    return Response(api_urls)

