from contextlib import nullcontext
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import *
import json
import datetime
from .forms import *
# Create your views here.
#start add to cart function
def cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items =order.orderitem_set.all()
    cartItems = order.get_cart_items
    return render(request, "cart/cart.html", {'items':items,'order':order,'cartItems':cartItems})

def checkout(request):
    customer = request.user
    
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items =order.orderitem_set.all()
    cartItems = order.get_cart_items

    if request.method == "POST":
            form = shipping(request.POST)
            transaction_id=datetime.datetime.now().timestamp()
            order.transaction_id=transaction_id
            if transaction_id != None:
                order.complete= True
            order.save()

            # cartItems.quantity
            
            form.save()
            return redirect("/dash")
    
    return render(request,'cart/checkout.html',{'items':items,'order':order, 'cartItems':cartItems})

def updateItem(request):
    data = json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print("Action:",action)
    print("productId:", productId)

    customer =request.user
    product= AddBook.objects.get(book_id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created =OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        if  orderItem.quantity==product.quantity:
            print("stock full")
            messages.error(request, "out of stock")
        else:
            orderItem.quantity=(orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity=(orderItem.quantity - 1)

  
    orderItem.save()

   
    if orderItem.quantity <=0:
        orderItem.delete()


        
    return JsonResponse('responseData', safe=False)

# to remove
def remove_order(request, p_id):
    orders = OrderItem.objects.filter(product_id=p_id)
    orders.delete()
 
    return redirect("/cart")

#to remove all items from cart
def delete_order(request, p_id):
    orders = Order.objects.filter(id=p_id)
    orders.delete()
 
    return redirect("/dash")

def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    date=json.loads(request.body)
    customer=request.user
  
    return JsonResponse('paymennt sucessful', safe=False)



#display orders done by user
def order_display(request,id):
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    orders=ShippingAddress.objects.filter(customer_id=id)
    order2=Order.objects.filter(customer_id=id)
    order3=OrderItem.objects.filter(order_id=id)
    # cartItems = order.get_cart_items
    
    return render(request,'orders.html',{'orders':orders,'order2':order2,'order3':order3,'cartItems': cartItems})#

#display books detail user had purchased
def Orderbook_details(request,id):
    orders=ShippingAddress.objects.filter(customer_id=id)
    order2=Order.objects.filter(customer_id=id)
    order3=OrderItem.objects.filter(order_id=id)
   
    # cartItems = order.get_cart_items
    
    return render(request,'show_books.html',{'orders':orders,'order2':order2,'order3':order3})
    
#delete order by user
def order_delete(request,id):
    user = Order.objects.get(id= id)
    user.delete()
    return redirect("/dash")
