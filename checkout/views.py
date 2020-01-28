from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm, SecondOrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from packages.models import Package
from django.contrib.auth.models import User
from accounts.models import Profile
import stripe

# Stripe api key
stripe.api_key = settings.STRIPE_SECRET

# Checkout view
@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        second_order_form = SecondOrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and second_order_form.is_valid() and payment_form.is_valid():
            order = second_order_form.save(commit=False)
            order.first_name = order_form.cleaned_data['first_name']
            order.last_name = order_form.cleaned_data['last_name']
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                package = get_object_or_404(Package, pk=id)
                total += quantity * package.price
                order_line_item = OrderLineItem(
                    order = order,
                    package = package, 
                    quantity = quantity
                    )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                user = request.user
                package = get_object_or_404(Package, pk=id)
                send_mail('Uber hosting order details', 'Congratulations\r\n\r\nYou have succesfully ordered your hosting package and will receive further information within the next 24 hours.\r\n\r\nName: {0} {1}\r\nYour package: {2}\r\nPaid amount: €{3}'.format(order.first_name, order.last_name, package.name, total), 'rkaal7@gmail.com', [user.email], fail_silently=False)
                
                messages.success(request, "You have successfully paid! An email has been send to you with further information.")
                request.session['cart'] = {}
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm(instance=request.user)
        second_order_form = SecondOrderForm(instance=request.user.profile)
        
    return render(request, "checkout.html", {'order_form': order_form, 'second_order_form': second_order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
