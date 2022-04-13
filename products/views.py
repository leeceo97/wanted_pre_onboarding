from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from products.models import Product, Sponsor
from products.serializers import ProductListSerializer, ProductDetailSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        else:
            return ProductSerializer

    @action(detail=True, methods=['post'])
    def funding(self, request, pk):
        Sponsor.objects.create(sponsor=request.user, product__id=pk)
        res = {
            'message': 'create'
        }
        return Response(res, status.HTTP_201_CREATED)