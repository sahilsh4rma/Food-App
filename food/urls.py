from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
   # index = '/food'
    path('',views.index,name="index"),

    # hello
    # path('item/',views.item,name="hello")


    #detail = '/food/<item_id>
    path('<int:item_id>/',views.detail,name="detail"),


    # add form
    path('add/',views.create_item,name="create_item"),

    # updatin item
    path('update/<int:id>/',views.update_item,name="update_item"),

    # delete an item
    path('delete.<int:id>/',views.delete_item,name="delete_item"),
]