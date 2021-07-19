from django.urls import path

from products.views import ProductsListView, ProductDetailView, WishListListView, add_wishlist, add_to_cart, \
    CartListView

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('wishlist/', WishListListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', add_wishlist, name='add-wishlist'),
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('', ProductsListView.as_view(), name='list'),
]
