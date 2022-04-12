# pup/orders/views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView

from .models import Product, Customer, Status, ProductOrder, Order


def home_view(request):
    context = {'page_title': "HOME"}
    return render(request, 'home.html', context)


class OrdersList(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class OrdersDetails(DetailView):
    template_name = 'orders/order_details.html'
    model = ProductOrder
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super(OrdersDetails, self).get_context_data(**kwargs)
        context['products'] = ProductOrder.objects.filter(order_id=self.kwargs['pk'])
        context['order'] = Order.objects.get(pk=self.kwargs['pk'])
        return context


def delete_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Order, id=pk)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/orders")

    return render(request, "orders/order_confirm_delete.html", context)