from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from products.models import Product, Sponsor
from products.serializers import ProductListSerializer, ProductDetailSerializer, ProductSerializer, FundingSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ('title',)

    def get_queryset(self):
        ordering = self.request.query_params.get('order_by', None)
        if self.action == 'list':
            if ordering == '생성일':
                return Product.objects.all().order_by('-created_at')
            elif ordering == '총펀딩금액':
                return Product.objects.all().order_by('-total_amount')
            else:
                return Product.objects.all()
        else:
            return Product.objects.all()

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