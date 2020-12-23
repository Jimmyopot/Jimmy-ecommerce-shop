from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib import messages

from .forms import PaymentForm
from core.models import Item, OrderItem, Order, PaymentAddress


class PaymentView(View):
    def get(self, *args, **kwargs):
        form = PaymentForm()
        context = {
            'form': form
        }        
        return render(self.request, "checkout-page.html", context)
    
    def post(self, *args, **kwargs):
        form = PaymentForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                county = form.cleaned_data('county')
                street_address = form.cleaned_data('street_address')        
                country = form.cleaned_data('country')
                zip = form.cleaned_data('zip')
                # same_shipping_address = form.cleaned_data('same_billing_address')
                # save_info = form.cleaned_data('save_info')
                payment_option = form.cleaned_data('payment_option')
                payment_address = PaymentAddress( 
                    user=self.request.user,
                    county=county,
                    street_address=street_address,
                    country=country,
                    zip=zip,        
                )
                payment_address.save()
                order.payment_address = payment_address
                
                return redirect("payment:payment")
            messages.warning(self.request, "Failed payment")
            
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("core:order-summary")
        
        
class PaymentOptionView(View):
    def get(self, *args, **kwargs):
               
        return render(self.request, "payment.html", {})
    