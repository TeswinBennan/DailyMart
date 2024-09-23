from django.urls import path
from.import views
urlpatterns = [
    path('',views.user1,name='user1'),
    path('contact',views.contact,name='contact'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('regdata',views.regdata,name='regdata'),
    path('logdata',views.logdata,name='logdata'),
    path('logout',views.logout,name='logout'),
    path('contactdata',views.contactdata,name='contactdata'),
    path('catview',views.catview,name='catview'),
    path('products/<str:category>/',views.products,name='products'),
    path('productdetail/<int:id>',views.productdetail,name='productdetail'),
    path('checkout1',views.checkout1,name='checkout1'),
    path('cart',views.cart,name='cart'),
    path('cartdata1/<int:id>',views.cartdata1,name='cartdata1'),
    path('cartdelete/<int:id>',views.cartdelete,name='cartdelete'),
    path('checkoutdata',views.checkoutdata,name='checkoutdata'),
    path('sucess',views.sucess,name='sucess'),
    path('about',views.about,name='about')
]
