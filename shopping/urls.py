from django.urls import path
from .views import (
    ShoppingPage,
    MakeOrder
)
urlpatterns = [
    path('', ShoppingPage, name='home'),
    path('make-order/<str:pk>', MakeOrder, name='make-order'),

]