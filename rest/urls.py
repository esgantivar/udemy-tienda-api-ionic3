from django.urls import path, include

from rest import views

urlpatterns = [
    path('lineas', views.LineasView.as_view(), name='lienas'),
    path('productos/todos', views.ProductsView.as_view(), name='products'),
    path('productos/todos/<int:page>', views.ProductsView.as_view(), name='products-page'),
    path('productos/<int:tipo>/<int:page>', views.ProductByCategoryView.as_view(), name='products-category'),
    path('productos/buscar/<str:term>', views.ProductSearchView.as_view(), name='products-search'),
    path('productos/<str:codigo>', views.ProductDetailView.as_view(), name='product-detail'),
    path('orden', views.OrderView.as_view(), name='order'),
    path('orden/<int:order_id>', views.OrderView.as_view(), name='order-delete'),
    path('orden/todas', views.OrdersView.as_view(), name='orders')
]
