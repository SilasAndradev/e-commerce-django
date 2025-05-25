from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from shopping.models import Order

@login_required(login_url='/login')
def DashboardModerator(request):
    if request.user.is_staff:
        orders = Order.objects.filter(delivery_confimation=False)

        context = {
            'orders':orders
        }
        
        return render(request, '', context)
    else:
        return redirect('home')