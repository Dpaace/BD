from django.urls import path, include
from register import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name='home'),

    path("Register", views.Register, name='register'),
    path("loginn", views.loginn, name='loginn'),
    path("dash", views.maindash, name='dash'),
    path("profile", views.profile, name='profile'),
    path("logout", views.logout_page, name='logout'),



    # Passeord Reset Section
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password/password_reset_form.html'),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password/password_reset_complete.html'),
         name='password_reset_complete'),


    # Important Function Defined
    path('afterlogin', views.afterlogin_view, name='afterlogin'),

    # path("adminlog", views.Aloginn, name='adminlog'),
    path("admindash", views.adminDashboard, name='admindash'),
    path("addbook", views.addbooks, name='addbook'),

    path("mybook", views.mybook),
    path("profile_setting", views.psetting),
    path("about/", views.about),

    path("edit/<int:p_id>", views.Bedit),
    path("delete/<int:p_id>", views.Bdelete),
    path("contact", views.contact),
    path("bookdesc/<slug>", views.viewbook),
    path("favourite/<int:id>", views.fav_post),
    path("favourite_list", views.favourite_list),
    path("contact", views.contact),
    path('searched', views.srch),
    path("delacc/<int:id>", views.acc_del),
    path('blogs', views.blog),
    path("range", views.price_range),
    path('shop', views.shop),

    path('fiction', views.fiction),
    path('nonfiction', views.nonfiction),
    path('philosophical', views.philosophical),
    path('thriller', views.thriller),
    path('romance', views.romance),

    path('customers', views.customers),
    path("cdelete/<int:p_id>", views.cdelete),
    path('user_order', views.user_order, name="user_order"),
    path('delivery_update/', views.delivery_update, name='delivery_update'),
    path('show_products/', views.show_products, name='show_products'),
    path('addDetails/<int:userid>', views.addDetails),
    path('updateProf/<int:id>', views.updateProf),

    path('customers',views.customers),
    path("cdelete/<int:p_id>",views.cdelete),
    path('user_order',views.user_order, name="user_order"),
    path('delivery_update/',views.delivery_update, name='delivery_update'),
    path('show_products/',views.show_products, name='show_products'),
    path("mybook/<int:id>", views.mybook),
    path('completeOrder',views.completeOrder),
    path('customers', views.customers),
    path("cdelete/<int:p_id>", views.cdelete),
    path('user_order', views.user_order, name="user_order"),
    path('delivery_update/', views.delivery_update, name='delivery_update'),
    path('show_products/', views.show_products, name='show_products'),
    path("mybook", views.mybook),
    path('completeOrder', views.completeOrder),
    path('team', views.team),
    path('aboutus', views.aboutus),
    path("adminpage",views.adminpage,name="adminpage"),
    path("message",views.message)
]
    

