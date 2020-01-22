from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    # Shows everything that is in the cart session.
    return render(request, "cart.html")

def add_to_cart(request, id):
    # Add package to cart session.
    quantity = 1
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def adjust_cart(request, id):
    # Adjust the packages in the cart session.
    quantity = 0
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))