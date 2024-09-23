from django.urls import path
from.import views
urlpatterns = [
    path('admin1',views.admin1,name='admin1'),
    path('category',views.category,name='category'),
    path('catdata',views.catdata,name='catdata'),
    path('table',views.table,name='table'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('productdata',views.productdata,name='productdata'),
    path('producttable',views.producttable,name='producttable'),
    path('edit1/<int:id>',views.edit1,name='edit1'),
    path('delete1/<int:id>',views.delete1,name='delete1'),
    path('update1/<int:id>',views.update1,name='update1'),
    path('contacttable',views.contacttable,name='contacttable'),
    path('registertable',views.registertable,name='registertable'),
    path('checkouttable1',views.checkouttable1,name='checkouttable1')
]
