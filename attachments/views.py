from rest_framework import generics

from attachments.models import Attachment
from attachments.serializers import AttachmentSerializer
from djangoKR_shop_v1.mypermission import IsAdminUserOrReadOnly


class AttachmentList(generics.ListCreateAPIView):
    # schema = AuthorListutoSchema(tags=['attachments'])
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    # pagination_class = SGPagination
    permission_classes = (IsAdminUserOrReadOnly,)


class AttachmentDetail(generics.RetrieveUpdateDestroyAPIView):
    # schema = AutoSchema(tags=['attachments'])
    lookup_field = 'uuid'
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

