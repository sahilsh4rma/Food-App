from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import Itemform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    item_list = Item.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != "" and item_name is not None:
         item_list = item_list.filter(item_name__icontains = item_name)
    paginator = Paginator(item_list,4)
    page = request.GET.get('page')
    item_list = paginator.get_page(page)

    return render(request,'food/index.html',{'item_list':item_list})


# detail view


class DetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html'


#creating a new item

class CreateItem(CreateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    template_name = 'food/forms-item.html'



#updatin Item

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