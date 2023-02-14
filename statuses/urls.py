from django.urls import path

from statuses.views import StatusList, StatusDetail

urlpatterns = [
    path('', StatusList.as_view()),
    path('<uuid>', StatusDetail.as_view()),
]