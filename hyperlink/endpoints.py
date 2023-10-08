from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

#API ROOT
@api_view(["GET"])
def api_hyperlink(request, format=None, pk=1):
    """Function to define api root view"""
    return Response(
        {
           'Seller': {
                #SELLER
                "seller": reverse("seller", request=request, format=format),
            
                "seller-detail": reverse(
                    "seller-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "seller-create": reverse(
                    "seller-create", request=request, format=format
                ),
            
                "seller-update": reverse(
                    "seller-update", kwargs={'pk': pk}, request=request, format=format
                ),

                "seller-delete": reverse(
                    "seller-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },

            'Buyer': {
                #BUYER
                "buyer": reverse("buyer", request=request, format=format),
            
                "buyer-detail": reverse(
                    "buyer-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "buyer-create": reverse(
                    "buyer-create", request=request, format=format
                ),

                "buyer-delete": reverse(
                    "buyer-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },

            'Company' : {
                #COMPANY 
                "company": reverse("company", request=request, format=format),
            
                "company-detail": reverse(
                    "company-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "company-create": reverse(
                    "company-create", request=request, format=format
                ),
            
                "company-update": reverse(
                    "company-update", kwargs={'pk': pk}, request=request, format=format
                ),

                "company-delete": reverse(
                    "company-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },

            'Hyperlink' : {
                #HYPERLINK
                "hyperlink": reverse("hyperlink", request=request, format=format),
            
                "hyperlink-detail": reverse(
                    "hyperlink-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "hyperlink-create": reverse(
                    "hyperlink-create", request=request, format=format
                ),
            
                "hyperlink-update": reverse(
                    "hyperlink-update", kwargs={'pk': pk}, request=request, format=format
                ),

                "hyperlink-delete": reverse(
                    "hyperlink-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },
            
            'Access Code' : {
                #ACCESS CODE
                "access-code": reverse("access-code", request=request, format=format),
            
                "access-code-detail": reverse(
                    "access-code-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "access-code-create": reverse(
                    "access-code-create", request=request, format=format
                ),
            
                "access-code-update": reverse(
                    "access-code-update", kwargs={'pk': pk}, request=request, format=format
                ),

                "access-code-delete": reverse(
                    "access-code-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },

            'Product' : {
                #PRODUCT
                "product": reverse("product", request=request, format=format),
            
                "product-detail": reverse(
                    "product-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "product-create": reverse(
                    "product-create", request=request, format=format
                ),
            
                "product-update": reverse(
                    "product-update", kwargs={'pk': pk}, request=request, format=format
                ),

                "product-delete": reverse(
                    "product-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },

            'Cart': {
                #CART 
                "cart": reverse("cart", request=request, format=format),
            
                "cart-detail": reverse(
                    "cart-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "cart-create": reverse(
                    "cart-create", request=request, format=format
                ),
            
                "cart-update": reverse(
                    "cart-update", kwargs={'pk': pk}, request=request, format=format
                ),

                "cart-delete": reverse(
                    "cart-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },
            
            'Cart Item': {
                #CART ITEM
                 "cart-item": reverse("cart-item", request=request, format=format),
            
                "cart-item-detail": reverse(
                    "cart-item-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "cart-item-create": reverse(
                    "cart-item-create", request=request, format=format
                ),
            
                "cart-item-update": reverse(
                    "cart-item-update", kwargs={'pk': pk}, request=request, format=format
                ),

                "cart-item-delete": reverse(
                    "cart-item-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },

            'Placed Product': {
                #PLACED PRODUCT
                "placed-product": reverse("placed-product", request=request, format=format),
            
                "placed-product-detail": reverse(
                    "placed-product-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "placed-product-create": reverse(
                    "placed-product-create", request=request, format=format
                ),

                "placed-product-delete": reverse(
                    "placed-product-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },

            'Purchased Order': {
                #PURCHASED ORDER
                "purchased-order": reverse("purchased-order", request=request, format=format),
            
                "purchased-order-detail": reverse(
                    "buyer-detail", kwargs={'pk': pk}, request=request, format=format
                ),
            
                "purchased-order-create": reverse(
                    "purchased-order-create", request=request, format=format
                ),

                "purchased-order-delete": reverse(
                    "purchased-order-delete", kwargs={'pk': pk}, request=request, format=format
                ),
            },

            'Authentication' : {
                #LOGIN
                "login" : reverse("login", request=request, format=format),

                #REGISTER
                "register" : reverse("register", request=request, format=format),

                #USER-DETAIL
                "user"  : reverse("user", request=request, format=format)
            },
        }
    )