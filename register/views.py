from pickle import FALSE
import re
from django.shortcuts import get_object_or_404, render, redirect
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from register.forms import *
from register.models import AddBook
from django.contrib import messages
from django.template.loader import render_to_string
import os
from register.models import AddBook
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from cart.models import *
from django.http import JsonResponse
import json
from . import models

# Create your views here.


def home(request):
    dash = AddBook.objects.raw("select * from addbook")
    return render(request, "homepage.html",{"dash":dash})


def Register(request):
    if request.method == 'POST':
        Username = request.POST['user_name']
        email = request.POST['email']
        psw = request.POST['psw']
        cpsw = request.POST['con_psw']
        first = request.POST['first']
        last = request.POST['last']
        if psw == cpsw:
            if User.objects.filter(username=Username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=Username, email=email, password=psw, first_name=first, last_name=last)
                    user.save()
                    messages.success(
                        request, 'You are registered successfully')
                    # return redirect('signin/signin.html')
                    return redirect("home")
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, "signin/signin.html")


def loginn(request):
    if request.method == 'POST':
        customer_name = request.POST.get("user_name")
        customer_password = request.POST.get("psw")
        user = authenticate(request, username=customer_name,
                            password=customer_password)
        if user is not None:
            login(request, user)
            return redirect("dash")
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('loginn')
    return render(request, "signin/signin.html")


def logout_page(request):
    logout(request)
    request.session.clear()
    return redirect("home")
    # return render(request, "homepage.html")


@login_required(login_url='loginn')
def maindash(request):
    # ADD_cart function
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    # add_cart funtion end
    dash = AddBook.objects.raw("select * from addbook")

    return render(request, "maindash.html", {'dash': dash, 'cartItems': cartItems})


@login_required
def afterlogin_view(request):
    if request.user.is_superuser:
        return redirect('adminpage')
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('adminlog')


# genre tempalates
def fiction(request):
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    dash = AddBook.objects.raw("select * from addbook")
    fiction = AddBook.objects.filter(b_genre="Fiction")
    return render(request, "genre/fiction.html", {'dash': dash, 'fiction': fiction,'cartItems': cartItems})


def nonfiction(request):
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    dash = AddBook.objects.raw("select * from addbook")
    nonfiction = AddBook.objects.filter(b_genre="Non-Fiction")
    return render(request, "genre/nonfiction.html", {'dash': dash, 'nonfiction': nonfiction,'cartItems': cartItems})


def philosophical(request):
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    dash = AddBook.objects.raw("select * from addbook")
    philosophical = AddBook.objects.filter(b_genre="Philosophical")
    return render(request, "genre/philosophical.html", {'dash': dash, 'philosophical': philosophical,'cartItems': cartItems})


def thriller(request):
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    dash = AddBook.objects.raw("select * from addbook")
    thriller = AddBook.objects.filter(b_genre="Thriller")
    return render(request, "genre/thriller.html", {'dash': dash, 'thriller': thriller,'cartItems': cartItems})


def romance(request):
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    dash = AddBook.objects.raw("select * from addbook")
    romance = AddBook.objects.filter(b_genre="Romance")
    return render(request, "genre/romance.html", {'dash': dash, 'romance': romance,'cartItems': cartItems})

# @login_required(login_url='afterlogin')


def adminpage(request):
    customer=User.objects.count()
    books=AddBook.objects.count()
    order=ShippingAddress.objects.count()
    msg=Contact.objects.count()
    return render(request,"admin_final/dashboard.html",{'customer':customer,'books':books,'order':order,'msg':msg})
def adminDashboard(request):
    if request.user.is_superuser:
        dash = AddBook.objects.raw("select * from addbook")
        return render(request, "admin_final/books.html", {'dash': dash})
    else:
        # messages.error(request, "Invalid login credentials")
        return redirect('adminlog')


def addbooks(request):
    if request.method == "POST":
        form = add_book(request.POST, request.FILES)
        form.save()
        return redirect("/admindash")
    return render(request, "admin_final/Add_book.html")

#to update the books by admin
def Bedit(request, p_id):  
    books = AddBook.objects.get(book_id=p_id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(books.b_pic) > 0:
                os.remove(books.b_pic.path)
            books.b_pic = request.FILES['b_pic']
        form = add_book(request.POST, instance=books)

        form.save()
        messages.success(request, "data has been updated ")
        return redirect("/admindash")
    return render(request, "admin_final/update.book.html", {'books': books})

#to delete the books by admin
def Bdelete(request, p_id):  
    books = AddBook.objects.get(book_id=p_id)
    books.delete()
    messages.success(request, "data has been deleted ")
    return redirect("/admindash")

# display all orders on admin page
def user_order(request):  # Show_order
    orders = ShippingAddress.objects.raw("select * from cart_shippingaddress")
    order3 = OrderItem.objects.raw("select * from cart_orderitem ")
    return render(request, 'admin_final/admin orders.html', {'orders': orders, 'order3': order3})

# update the status of shippping order
def delivery_update(request):
    data = json.loads(request.body)
    orderId = data['orderId']
    action = data['action']

    print("Action:", action)
    print("orderId:", orderId)

    delivery = ShippingAddress.objects.get(id=orderId)
    if action == 'update':
        delivery.status = True
        print('success')
        delivery.save()
    return JsonResponse("complete order", safe=False,)

# display book_details purchased by customer on admin side
def show_products(request):
    data = json.loads(request.body)
    orderId = data['itemsid']
    action = data['action']

    print("Action:", action)
    print("orderId:", orderId)

    if action == "show":
        books = OrderItem.objects.filter(order_id=orderId)

    return JsonResponse({'books': books}, safe=False,)

def completeOrder(request):
    orders=ShippingAddress.objects.filter(status=True)
    return render(request,'Admin/completed_order.html',{'orders':orders})



# user detail on admin side
def customers(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'admin_final/customers.html', {'users': users, })

#to remove customer
def cdelete(request, p_id):
    users = User.objects.get(id=p_id)
    users.delete()
    messages.success(request, "data has been deleted ")
    return render(request, 'admin_final/customers.html')

#to see message from users
def message(request):
    msg=Contact.objects.raw("select * from contact")
    return render(request,"admin_final/messages.html",{'msg':msg})

# profile page


def profile(request):
    
    details = UserP.objects.get(id = request.user.id)
    c_id=request.user.id
   
    return render(request, "User/profile.html",{'details':details,'c_id':c_id})


def addDetails(request, userid):
    customer = models.User.objects.get(id = userid)
    if request.method == "POST":
        forms = Update_form(request.POST, request.FILES)
        forms.save()
        return redirect("/profile")
    return render(request, "User/addDetails.html", {'customer': customer})

def updateProf(request, id):
    details = UserP.objects.get(id = id)
    if request.method == "POST":
        forms = Update_form(request.POST, request.FILES, instance = details )
        forms.save()
        return redirect("/about")
    return render(request, 'User/updateProf.html', {'details': details})

def mybook(request):
    new = AddBook.newmanager.filter(favourite=request.user)
    # cartItems = order.get_cart_items
    
    return render(request,'User/mybooks.html',{'new':new})



def psetting(request):
    return render(request, "User/settings.html")


def about(request):
    
    details = UserP.objects.get(id = request.user.id)

    return render(request, "User/about.html", {'details':details})


def contact(request):
    if request.method == "POST":
        form = contact_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/dash")
            except:
                print("Invalid")

    return render(request, "User/contact_us.html")


# details about each book
def viewbook(request, slug):
    books = get_object_or_404(AddBook,New_slug=slug)
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items =order.orderitem_set.all()
    cartItems = order.get_cart_items
    
    is_favourite = bool
    if books.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    context = {
        'books': books,
        'is_favourite': is_favourite
    }
    return render(request, "viewbook.html", {'books': books, 'is_favourite': is_favourite,'cartItems':cartItems})
    
#adding into your favourite
def fav_post(request, id):
    post = get_object_or_404(AddBook, book_id=id)

    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)

    else:
        post.favourite.add(request.user)
    context = {
        'post': post,

    }

    return HttpResponseRedirect(request.META['HTTP_REFERER'], context)


def favourite_list(request):
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    new = AddBook.newmanager.filter(favourite=request.user)
    return render(request, "User/fav_list.html", {'new': new,'cartItems': cartItems})


# search bar
def srch(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = AddBook.objects.filter(b_name__icontains=searched)
        dash = AddBook.objects.raw("select * from addbook")
        return render(request, "search.html", {'searched': searched, 'venues': venues, 'dash': dash})
    else:
        return render(request, 'search.html')


def acc_del(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, "your account has been deleted ")
    return redirect("/")


def blog(request):
    return render(request, 'blogs.html')

def shop(request):
    customer = request.user
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    # add_cart funtion end
    dash = AddBook.objects.raw("select * from addbook")

    return render(request, 'shop.html', {'dash': dash, 'cartItems': cartItems})


def price_range(request):
    if request.method == "POST":
        price = request.POST('')
        
    
        return render(request, 'price_range.html')

def team(request):
    return render(request, "ourteam/ourteam.html")
def aboutus(request):
    return render(request, "About/about.html")

