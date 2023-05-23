from products.api.serializers import CategorySerializer, ProductSerializer, StocksSerializer
from products.models import Category, Product, Stock

def get_categories_service():
    try:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return serializer.data
    except:
        raise RuntimeError("product_services > get_categories_service: something went wrong.")
    
def get_products_service(request):
    try:
        search_query = request.query_params.get('q')
        category = request.query_params.get('category')
        is_cash_on_delivery_available = request.query_params.get('isCashOnDeliveryAvailable')

        products = Product.objects.all().order_by('-created_at')

        if search_query != None:
            products = products.filter(title__icontains=search_query)

        if category != None:
            products = products.filter(category__slug=category)

        if is_cash_on_delivery_available != None and is_cash_on_delivery_available == 'true':
            products = products.filter(is_cash_on_delivery_available=True)

        serializer = ProductSerializer(products, many=True)
        return serializer.data
    except Exception as e:
        raise RuntimeError(f"product_services > get_products_service: {e}")

def get_product_details_service(request, product_id):
    try:
        products = Product.objects.get(pk=product_id)

        serializer = ProductSerializer(products)
        return serializer.data
    except Exception as e:
        raise RuntimeError(f"product_services > get_product_details_service: {e}")

def get_stock_service(request, product_id):
    try:
        stocks = Stock.objects.get(product__id=product_id)

        serializer = StocksSerializer(stocks)
        return serializer.data
    except Exception as e:
        raise RuntimeError(f"product_services > get_stock_service: {e}")
  