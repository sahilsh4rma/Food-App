from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
   # index = '/food'
    # path('',views.IndexClassView.as_view(),name="index"),

    path('',views.index,name="index"),

    #detail = '/food/<item_id>
    path('<int:pk>/',views.DetailClassView.as_view(),name="detail"),


    # add form
    path('add/',views.CreateItem.as_view(),name="create_item"),

    # updatin item
    path('update/<int:id>/',views.update_item,name="update_item"),

    # delete an item
    path('delete.<int:id>/',views.delete_item,name="delete_item"),
]