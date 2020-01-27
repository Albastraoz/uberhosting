from django.shortcuts import render, reverse, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method=="POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['full_name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            send_mail('Uber hosting contact form', '{0} send the following message through the contact form:\r\n\r\n{1}'.format(name, message), email, ['rkaal7@gmail.com'], fail_silently=False)
            messages.success(request, "Message has been send! We will reply you shortly.")

            return redirect(reverse('contact'))

    else:
        contact_form = ContactForm()
    return render(request, "contact.html", {'contact_form': contact_form})