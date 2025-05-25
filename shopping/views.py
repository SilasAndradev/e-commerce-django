from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .models import Product 
from accounts.models import Client
from .forms import OrderForm

def ShoppingPage(request):

    context = {
        'product':Product.objects.all()
    }

    return render(request, '', context)

@login_required(login_url='/login')
def MakeOrder(request, pk):
    client = Client.objects.get(user=request.user)
    product = Product.objects.get(id=pk)
    if client.IsBlock:
        return redirect('home')
    else:
        form = OrderForm()
        
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid:
                order = form.save(commit=False)
                order.client = client
                order.product = product
                order.save()
                return