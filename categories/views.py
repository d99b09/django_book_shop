from rest_framework import generics

from categories.models import Category
from categories.serializers import CategorySerializer
from djangoKR_shop_v1.mypermission import IsAdminUserOrReadOnly
from djangoKR_shop_v1.pagination import SGPagination


class CategoryList(generics.ListCreateAPIView):
    # schema = AuthorListutoSchema(tags=['attachments'])
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = SGPagination
    permission_classes = (IsAdminUserOrReadOnly,)




class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # schema = AutoSchema(tags=['attachments'])
    lookup_field = 'uuid'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)

