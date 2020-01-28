from django.shortcuts import render, reverse, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Send email to owner email address when contact form is send
def contact(request):
    if request.method=="POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['full_name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            send_mail('Uber hosting contact form', 'Someone seeks contact from Uberhosting\r\n\r\nName: {0}\r\nEmail: {1}\r\n\r\nMessage:\r\n{2}'.format(name, email, message), email, ['rkaal7@gmail.com'], fail_silently=False)
            messages.success(request, "Message has been send! We will reply you shortly.")

            return redirect(reverse('contact'))

    else:
        contact_form = ContactForm()
    return render(request, "contact.html", {'contact_form': contact_form})