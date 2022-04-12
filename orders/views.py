# pup/orders/views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView

from .models import Product, Customer, Status, ProductOrder, Order


def home_view(request):
    context = {'page_title': "HOME"}
    return render(request, 'home.html', context)


class OrdersList(ListView):
    model = Order
    template_name = 'orders/designer_dashboard.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

