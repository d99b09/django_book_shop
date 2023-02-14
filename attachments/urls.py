from django.urls import path

from attachments.views import AttachmentList, AttachmentDetail

urlpatterns = [
    path('', AttachmentList.as_view()),
    path('<uuid>', AttachmentDetail.as_view()),
]