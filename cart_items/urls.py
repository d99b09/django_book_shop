from django.urls import path

from cart_items.views import Cart_itemList, Cart_itemDetail

urlpatterns = [
    path('', Cart_itemList.as_view()),
    path('<uuid>', Cart_itemDetail.as_view()),
]