from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import Itemform

# Create your views here.



def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        "item_list":item_list
    }
    # return HttpResponse(template.render(context,request))
    return render(request,'food/index.html',context)

# def item(request):
#     return HttpResponse("this is an item")


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        "item":item,
    }
    return render(request,'food/detail.html',context)
    # return HttpResponse("this is item_id: %s" % item_id)

def create_item(request):
    form = Itemform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return  render(request,'food/forms-item.html',{"form":form})


# updating an existing item

def update_item(request,id):
    item = Item.objects.get(pk=id)
    form = Itemform(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/forms-item.html',{"form":form, "item":item})

# deleting an item

def delete_item(request,id):
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return(render(request,'food/delete-item.html',{"item":item}))