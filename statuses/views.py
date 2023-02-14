from rest_framework import generics

from djangoKR_shop_v1.mypermission import IsAdminUserOrReadOnly
from statuses.models import Status
from statuses.serializers import StatusSerializer


class StatusList(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAdminUserOrReadOnly,)



class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uuid'
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
