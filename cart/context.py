from django.shortcuts import get_object_or_404
from packages.models import Package

def cart_contents(request):
    # Makes contents of cart available.

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    package_count = 0
    for id, quantity in cart.items():
        package = get_object_or_404(Package, pk=id)
        total += quantity * package.price
        package_count += quantity
        cart_items.append({'id':id, 'quantity': quantity, 'package': package})

    return { 'cart_items': cart_items, 'total': total, 'package_count': package_count }