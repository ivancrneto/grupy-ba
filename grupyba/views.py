# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

def home(request):
    return render_to_response('home.html')

def send_contact_mail(request):

    if request.method == 'POST':
        from grupyba.forms import ContactForm   
        from django.core.mail import send_mail

        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['issue'] + "_" + cd['name'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['ivan.cr.neto@gmail.com'],
                fail_silently=False
            )           
    return render_to_response('contact_sent.html')   

@csrf_protect
def contact(request):
    from grupyba.forms import ContactForm    

    contact_form = ContactForm()
    
    if request.method == 'POST': 
        contact_form = ContactForm(request.POST)        
    if contact_form.is_valid():
        return send_contact_mail(request)  
    
    return render_to_response('contact.html', locals(), context_instance=RequestContext(request)) 
