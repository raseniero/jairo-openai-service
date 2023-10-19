from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from . models import Seller, Buyer, Company, Hyperlink, Access_Code, Product, Placed_Product, Purchased_Order, Cart, Cart_Item
from . serializers import SellerSerializer, BuyerSerializer, CompanySerializer, HyperlinkSerializer, CodeSerializer, ProductSerializer, PlacedProductSerializer, PurchasedOrderSerializer, CustomAuthTokenSerializer, RegisterSerializer, CartSerializer, CartItemSerializer
from rest_framework import status

#fetch all sellers
@api_view(['GET'])
def getSellerList(request):
    try:
        seller = Seller.objects.all()
        serializer = SellerSerializer(seller, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        password = request.data['password']
        hashed_password = make_password(password)
        request.data['password'] = hashed_password 
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update a seller info
@api_view(['PUT'])
def sellerUpdate(request, pk):
    try:
        seller = Seller.objects.get(id=pk)
        serializer = SellerSerializer(instance=seller, data=request.data)
        password = request.data['password']
        hashed_password = make_password(password) 
        request.data['password'] = hashed_password  
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


#fetch all buyers
@api_view(['GET'])
def getBuyerList(request):
    try:
        buyer = Buyer.objects.all()
        serializer = BuyerSerializer(buyer, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# fetch a single buyer
@api_view(['GET'])
def getBuyerDetail(request, pk):
    try:
        buyer = Buyer.objects.get(id=pk)
        serializer = BuyerSerializer(buyer, many=False)
        return Response(serializer.data)
    except Buyer.DoesNotExist:
        # Handle the case where the buyer with the given ID does not exist
        error_message = "Buyer with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# create a buyer    
@api_view(['POST'])
def buyerCreate(request):
    try:
        serializer = BuyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
# delete a buyer
@api_view(['DELETE'])
def buyerDelete(request, pk):
    try:
        buyer = Buyer.objects.get(id=pk)
        buyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Buyer.DoesNotExist:
        # Handle the case where the buyer with the given ID does not exist
        error_message = "Buyer with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)


#fetch all company
@api_view(['GET'])
def getCompanyList(request):
    try:
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
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
    

#fetch all hyperlinks
@api_view(['GET'])
def getHyperlinkList(request):
    try:
        hyperlink = Hyperlink.objects.all()
        serializer = HyperlinkSerializer(hyperlink, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# fetch a single hyperlink
@api_view(['GET'])
def getHyperlinkDetail(request, pk):
    try:
        hyperlink = Hyperlink.objects.get(id=pk)
        serializer = HyperlinkSerializer(hyperlink, many=False)
        return Response(serializer.data)
    except Hyperlink.DoesNotExist:
        # Handle the case where the hyperlink with the given ID does not exist
        error_message = "Hyperlink with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# create a hyperlink    
@api_view(['POST'])
def hyperlinkCreate(request):
    try:
        serializer = HyperlinkSerializer(data=request.data) 
        name = request.data['name'].split(' ')[0]
        url = request.data['url']
        concatenated_url = f'{url}{name}'
        request.data['url'] = concatenated_url 
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update a hyperlink info
@api_view(['PUT'])
def hyperlinkUpdate(request, pk):
    try:
        hyperlink = Hyperlink.objects.get(id=pk)
        serializer = HyperlinkSerializer(instance=hyperlink, data=request.data)
        name = request.data['name'].split(' ')[0]
        url = request.data['url']
        concatenated_url = f'{url}{name}'
        request.data['url'] = concatenated_url 
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Hyperlink.DoesNotExist:
        # Handle the case where the hyperlink with the given ID does not exist
        error_message = "Hyperlink with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)    

# delete a hyperlink
@api_view(['DELETE'])
def hyperlinkDelete(request, pk):
    try:
        hyperlink = Hyperlink.objects.get(id=pk)
        hyperlink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Hyperlink.DoesNotExist:
        # Handle the case where the hyperlink with the given ID does not exist
        error_message = "Hyperlink with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)
    

# fetch all access codes
@api_view(['GET'])
def getCodeList(request):
    try:
        access_code = Access_Code.objects.all()
        serializer = CodeSerializer(access_code, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# fetch a single access code
@api_view(['GET'])
def getCodeDetail(request, pk):
    try:
        access_code = Access_Code.objects.get(id=pk)
        serializer = CodeSerializer(access_code, many=False)
        return Response(serializer.data)
    except Access_Code.DoesNotExist:
        # Handle the case where the access code with the given ID does not exist
        error_message = "Access Code with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# create an access code    
@api_view(['POST'])
def codeCreate(request):
    try:
        serializer = CodeSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update an access code info
@api_view(['PUT'])
def codeUpdate(request, pk):
    try:
        access_code = Access_Code.objects.get(id=pk)
        serializer = CodeSerializer(instance=access_code, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Access_Code.DoesNotExist:
        # Handle the case where the access code with the given ID does not exist
        error_message = "Access Code with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)    

# delete an access code
@api_view(['DELETE'])
def codeDelete(request, pk):
    try:
        access_code = Access_Code.objects.get(id=pk)
        access_code.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Access_Code.DoesNotExist:
        # Handle the case where the access code with the given ID does not exist
        error_message = "Access Code with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)


# fetch all product
@api_view(['GET'])
def getProductList(request):
    try:
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# fetch a single product
@api_view(['GET'])
def getProductDetail(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        # Handle the case where the product with the given ID does not exist
        error_message = "Product with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# create a product    
@api_view(['POST'])
def productCreate(request):
    try:
        serializer = ProductSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update a product info
@api_view(['PUT'])
def productUpdate(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Product.DoesNotExist:
        # Handle the case where the product with the given ID does not exist
        error_message = "Product with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)    

# delete a product
@api_view(['DELETE'])
def productDelete(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        # Handle the case where the product with the given ID does not exist
        error_message = "Product with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)
    
# fetch all cart
@api_view(['GET'])
def getCartList(request):
    try:
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# fetch a single cart
@api_view(['GET'])
def getCartDetail(request, pk):
    try:
        cart = Cart.objects.get(id=pk)
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data)
    except Cart.DoesNotExist:
        # Handle the case where the cart with the given ID does not exist
        error_message = "Cart with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# create a cart   
@api_view(['POST'])
def cartCreate(request):
    try:
        serializer = CartSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update a cart info
@api_view(['PUT'])
def cartUpdate(request, pk):
    try:
        cart = Cart.objects.get(id=pk)
        serializer = CartSerializer(instance=cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Cart.DoesNotExist:
        # Handle the case where the cart with the given ID does not exist
        error_message = "Cart with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)    

# delete a cart
@api_view(['DELETE'])
def cartDelete(request, pk):
    try:
        cart = Cart.objects.get(id=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Cart.DoesNotExist:
        # Handle the case where the cart with the given ID does not exist
        error_message = "Cart with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)
    
# fetch all cart items
@api_view(['GET'])
def getCartItemList(request):
    try:
        cart_item = Cart_Item.objects.all()
        serializer = CartItemSerializer(cart_item, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# fetch a single cart item
@api_view(['GET'])
def getCartItemDetail(request, pk):
    try:
        cart_item = Cart_Item.objects.get(id=pk)
        serializer = CartItemSerializer(cart_item, many=False)
        return Response(serializer.data)
    except Cart_Item.DoesNotExist:
        # Handle the case where the cart item with the given ID does not exist
        error_message = "Cart Item with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# create a cart item   
@api_view(['POST'])
def cartItemCreate(request):
    try:
        serializer = CartItemSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update a cart item
@api_view(['PUT'])
def cartItemUpdate(request, pk):
    try:
        cart_item = Cart_Item.objects.get(id=pk)
        serializer = CartItemSerializer(instance=cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Cart_Item.DoesNotExist:
        # Handle the case where the cart item with the given ID does not exist
        error_message = "Cart Item with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)    

# delete a cart item
@api_view(['DELETE'])
def cartItemDelete(request, pk):
    try:
        cart_item = Cart_Item.objects.get(id=pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Cart_Item.DoesNotExist:
        # Handle the case where the cart item with the given ID does not exist
        error_message = "Cart Item with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

    
#fetch all placed products
@api_view(['GET'])
def getPlacedProductList(request):
    try:
        placed_product = Placed_Product.objects.all()
        serializer = PlacedProductSerializer(placed_product, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# fetch a single placed product
@api_view(['GET'])
def getPlacedProductDetail(request, pk):
    try:
        placed_product = Placed_Product.objects.get(id=pk)
        serializer = PlacedProductSerializer(placed_product, many=False)
        return Response(serializer.data)
    except Placed_Product.DoesNotExist:
        # Handle the case where the placed product with the given ID does not exist
        error_message = "Placed Product with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# create a placed product    
@api_view(['POST'])
def placedProductCreate(request):
    try:
        serializer = PlacedProductSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# delete a placed product
@api_view(['DELETE'])
def placedProductDelete(request, pk):
    try:
        placed_product = Placed_Product.objects.get(id=pk)
        placed_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Placed_Product.DoesNotExist:
        # Handle the case where the placed product with the given ID does not exist
        error_message = "Placed Product with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)


#fetch all purchased order
@api_view(['GET'])
def getPurchasedOrderList(request):
    try:
        purchased_order = Purchased_Order.objects.all()
        serializer = PurchasedOrderSerializer(purchased_order, many=True)
        return Response(serializer.data)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# fetch a single purchased order
@api_view(['GET'])
def getPurchasedOrderDetail(request, pk):
    try:
        purchased_order = Purchased_Order.objects.get(id=pk)
        serializer = PurchasedOrderSerializer(purchased_order, many=False)
        return Response(serializer.data)
    except Purchased_Order.DoesNotExist:
        # Handle the case where the purchased order with the given ID does not exist
        error_message = "Purchased Order with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)

# create a purchased order    
@api_view(['POST'])
def purchasedOrderCreate(request):
    try:
        serializer = PurchasedOrderSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
         return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# delete a buyer
@api_view(['DELETE'])
def purchasedOrderDelete(request, pk):
    try:
        purchased_order = Purchased_Order.objects.get(id=pk)
        purchased_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Purchased_Order.DoesNotExist:
        # Handle the case where the purchased order with the given ID does not exist
        error_message = "Purchased Order with ID {} does not exist".format(pk)
        return JsonResponse({'error': error_message}, status=404)


#authentication APIs

#data serializer #limits data output field to be shown 
def serialize_user(user):
    return {
        "id" : user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone_number" : user.phone_number 
    }


#login authentication and user-generated token
@api_view(['POST'])
def login(request):
    serializer = CustomAuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    print(user)
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'user_data': serialize_user(user),
        'token': token.key
    })
        

#register user authentication 
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user_info": serialize_user(user),
            "token": token.key
        })


#fetch user details given the correct token of that current user
@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_data': serialize_user(user)
        })
    return Response({})



