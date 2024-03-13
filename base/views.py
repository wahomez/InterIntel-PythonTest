from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductVariant

@api_view(['POST'])
def bulk_insert_products(request):
    data = request.data  # Assuming you send a list of dictionaries with product details

    try:
        # Bulk insert products
        products_to_create = [Product(name=item['name']) for item in data]
        created_products = Product.objects.bulk_create(products_to_create)

        # Create a dictionary mapping product names to product instances
        product_instance_dict = {product.name: product for product in created_products}

        # Now bulk insert product variants
        variants_to_create = []
        for item in data:
            product_instance = product_instance_dict[item['name']]
            variants = item.get('variants', [])  # Assuming variants are sent as a list
            for variant in variants:
                variants_to_create.append(ProductVariant(product=product_instance, name=variant['name'], price=variant['price'], sku=variant.get('sku')))

        ProductVariant.objects.bulk_create(variants_to_create)

        return Response({'message': 'Bulk insert successful'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
