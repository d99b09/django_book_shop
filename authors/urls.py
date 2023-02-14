from django.urls import path

from authors.views import AuthorList, AuthorDetail

urlpatterns = [
    path('', AuthorList.as_view()),
    path('<uuid>', AuthorDetail.as_view()),
]