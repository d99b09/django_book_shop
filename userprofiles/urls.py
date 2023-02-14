from django.urls import path

from userprofiles.views import UserProfileList, UserProfileDetail

urlpatterns = [
    path('', UserProfileList.as_view()),
    path('<uuid>', UserProfileDetail.as_view()),
]