from django.urls import path, include
from cart import views

#add to cart
urlpatterns = [
    path('update_item/',views.updateItem, name='update_item'),
    path('cart',views.cart, name='cart'),
    path('checkout',views.checkout, name='checkout'),
    path('process_order/',views.processOrder, name='process_order'),
    path('remove_order/<int:p_id>',views.remove_order, name='remove_order'),
    path('delete_order/<int:p_id>',views.delete_order, name='delete_order'),
    path('order_display/<int:id>',views.order_display, name='order_display'),
    path('orderbook_display/<int:id>',views.Orderbook_details, name='orderbook_display'),
    path('order_delete/<int:id>',views.delete_order, name='order_delete'),

]
