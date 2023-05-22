from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import logging

from products.api.services import product_services as service

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@api_view(['GET'])
def get_categories(request):
    response = {
        'body': None
    }
    try:
        categories = service.get_categories_service()
        response['body'] = {
            'categories': categories
        }
        response['message'] = "Categories received successfully!"
        logger.info(f"product_views > get_categories: {len(categories)} categories found.")
        return Response(response, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(f"product_views > get_categories: {e}")
        response['message'] = "Something went wrong!"
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_products(request):
    response = {
        'body': None
    }
    try:
        products = service.get_products_service(request)
        response['body'] = {
            'products': products
        }
        response['message'] = "Products received successfully!"
        logger.info(f"product_views > get_products: {len(products)} products found.")
        return Response(response, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(f"product_views > get_products: {e}")
        response['message'] = "Something went wrong!"
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_product_details(request, product_id):
    response = {
        'body': None
    }
    try:
        product = service.get_product_details_service(request, product_id)
        response['body'] = {
            'product': product
        }
        response['message'] = "Product received successfully!"
        logger.info(f"product_views > get_product_details: product details found.")
        return Response(response, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(f"product_views > get_product_details: {e}")
        response['message'] = "Something went wrong!"
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_stock(request, product_id):
    response = {
        'body': None
    }
    try:
        stock = service.get_stock_service(request, product_id)
        response['body'] = {
            'stock': stock
        }
        response['message'] = "Stock received successfully!"
        logger.info(f"product_views > get_stock: stock detials found.")
        return Response(response, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(f"product_views > get_stock: {e}")
        response['message'] = "Something went wrong!"
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
