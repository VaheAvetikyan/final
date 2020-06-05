from django.shortcuts import render, redirect

from .models import Order
from .validate import place_order


# Create your views here.
def history(request):
    user = request.user

    orders = Order.objects.filter(user=user)

    context = {
        'orders': orders,
    }

    return render(request,
                  "orders/history.html",
                  context)


def place(request):
    user = request.user

    if not user.address:
        return redirect("authentication:address")

    place_order(user)

    return redirect('orders:history')
