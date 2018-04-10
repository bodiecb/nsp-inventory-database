from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from django import forms

from .models import Item, Checkout
from .forms import ItemForm, PartialCheckoutForm

#Create your views here

class IndexView(generic.ListView):
    template_name = 'inventorydata/index.html'
    context_object_name = 'items_alphabetically'

    def get_queryset(self):
        return Item.objects.order_by('-item_text')[:10]

class CheckoutsView(generic.DetailView):
    model = Item
    template_name = 'inventorydata/checkouts.html'

def checkin(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    checkedin = False
    checkout_set = Checkout.objects.filter(item=item)
    for checkout in checkout_set:
        if checkout.return_date is None:
            checkout.return_date = timezone.now()
            checkout.save()
            checkedin = True
        
    if not checkedin:
        return render(request, 'inventorydata/checkouts.html', {
            'item': item,
            'error_message': "This item is already checked in.",
        })
    
    else:
        return render(request, 'inventorydata/checkouts.html', {'item' : item})

def checkout(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST' :
        new_checkout = Checkout(item=item)
        checkout_form = PartialCheckoutForm(request.POST, instance=new_checkout)
        if checkout_form.is_valid():
            checkout_form.save()
            return HttpResponseRedirect(reverse('inventorydata:checkouts', args=(item.id,)))
    
    else: 
        checkedout = False
        checkout_set = Checkout.objects.filter(item=item)
        for checkout in checkout_set:
            if checkout.return_date is None:
                checkedout = True
        
        if checkedout:
            return render(request, 'inventorydata/checkouts.html', {
            'item': item,
            'error_message': "This item is currently checked out.",
        })
        else:
            checkout_form = PartialCheckoutForm()
            return render(request, 'inventorydata/checkout.html', {'form' : checkout_form, 'item' : item})

def item(request):
    if request.method == 'POST' :
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item_form.save()
            return HttpResponseRedirect(reverse('inventorydata:index'))
    
    else: 
        item_form = ItemForm()
        return render(request, 'inventorydata/item.html', {'form' : item_form})


