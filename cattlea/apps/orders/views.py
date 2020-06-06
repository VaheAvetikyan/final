from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Order
from .validate import place_order


# Create your views here.
def history(request):
    user = request.user

    orders = Order.objects.filter(user=user).order_by('-pk')

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


def order_received(request):
    user = request.user

    id = request.POST.get('id')

    order = Order.objects.get(pk=id)

    # Set order as delivered
    order.delivered()
    order.save()

    data = {
        "order_id": order.id
    }

    return JsonResponse(data)
