from rest_framework import generics

from djangoKR_shop_v1.mypermission import IsAdminUserOrReadOnly
from djangoKR_shop_v1.pagination import SGPagination
from products.models import Product
from products.serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    # schema = AuthorListutoSchema(tags=['attachments'])
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = SGPagination
    permission_classes = (IsAdminUserOrReadOnly,)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    # schema = AutoSchema(tags=['attachments'])
    lookup_field = 'uuid'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

