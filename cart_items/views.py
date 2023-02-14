from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from cart_items.models import Cart_item
from cart_items.serializers import Cart_itemSerializer
from djangoKR_shop_v1.mypermission import IsAdminUserOrReadOnly


class Cart_itemList(generics.ListAPIView):
    queryset = Cart_item.objects.all()
    serializer_class = Cart_itemSerializer


class Cart_itemDetail(generics.RetrieveUpdateDestroyAPIView):
    # schema = AutoSchema(tags=['attachments'])
    lookup_field = 'uuid'
    queryset = Cart_item.objects.all()
    serializer_class = Cart_itemSerializer
