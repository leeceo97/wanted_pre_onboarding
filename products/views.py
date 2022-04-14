from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from products.models import Product, Sponsor
from products.serializers import ProductListSerializer, ProductDetailSerializer, ProductSerializer, FundingSerializer


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
        serializer = FundingSerializer(data=request.data, context={'request': request, 'pk':pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)