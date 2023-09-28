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

#fetch all seller
@api_view(['GET'])
def getSellerList(request):
    try:
        seller = Seller.objects.all()
        serializer = SellerSerializer(seller, many=True)
        return Response(serializer.data)
    except Exception as err:
        print(err)

# fetch a single seller
@api_view(['GET'])
def getSellerDetail(request, pk):
    try:
        seller = Seller.objects.get(id=pk)
        serializer = SellerSerializer(seller, many=False)
        return Response(serializer.data)
    except Seller.DoesNotExist:
        # Handle the case where the seller with the given ID does not exist
        error_message = "Seller with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# create a seller    
@api_view(['POST'])
def sellerCreate(request):
    try:
        serializer = SellerSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)

# update a seller info
@api_view(['PUT'])
def sellerUpdate(request, pk):
    try:
        seller = Seller.objects.get(id=pk)
        serializer = SellerSerializer(instance=seller, data=request.data)  
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Seller.DoesNotExist:
        # Handle the case where the seller with the given ID does not exist
        error_message = "Seller with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# delete a seller
@api_view(['DELETE'])
def sellerDelete(request, pk):
    try:
        seller = Seller.objects.get(id=pk)
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Seller.DoesNotExist:
        # Handle the case where the seller with the given ID does not exist
        error_message = "Seller with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)


#fetch all company
@api_view(['GET'])
def getCompanyList(request):
    try:
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)
    except Exception as err:
        print(err)


# fetch a single company
@api_view(['GET'])
def getCompanyDetail(request, pk):
    try:
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)
    except Company.DoesNotExist:
        # Handle the case where the company with the given ID does not exist
        error_message = "Company with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)
    

# create a company    
@api_view(['POST'])
def companyCreate(request):
    try:
        serializer = CompanySerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)


# update a company info
@api_view(['PUT'])
def companyUpdate(request, pk):
    try:
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(instance=company, data=request.data)  
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Company.DoesNotExist:
        # Handle the case where the company with the given ID does not exist
        error_message = "Company with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# delete a company
@api_view(['DELETE'])
def companyDelete(request, pk):
    try:
        company = Company.objects.get(id=pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Company.DoesNotExist:
        # Handle the case where the company with the given ID does not exist
        error_message = "Company with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)