from rest_framework import generics
from rest_framework.permissions import AllowAny

from authors.models import Author
from authors.serializers import AuthorSerializer
from djangoKR_shop_v1.mypermission import IsAdminUserOrReadOnly
from djangoKR_shop_v1.pagination import SGPagination


class AuthorList(generics.ListCreateAPIView):
    # schema = AuthorListutoSchema(tags=['attachments'])
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = SGPagination
    permission_classes = (IsAdminUserOrReadOnly,)



class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    # schema = AutoSchema(tags=['attachments'])
    lookup_field = 'uuid'
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

