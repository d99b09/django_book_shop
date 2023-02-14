from django.urls import path

from categories.views import CategoryList, CategoryDetail

urlpatterns = [
    path('', CategoryList.as_view()),
    path('<uuid>', CategoryDetail.as_view()),
]