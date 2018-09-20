from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

from .models import Person
from .forms import SubscribeForm

def home(request):
  
  if request.method == 'POST':
    
    form = SubscribeForm(request.POST)
    
    if form.is_valid():
       
        p = form.save()
        '''
        name = form.cleaned_data['name']
        number = form.cleaned_date['phone_number']
        p = Person(name=name, phone_number=number, date_subscribed=datetime.now(), messages_recieved=0)
        p.save()
        '''
        
        return HttpResponseRedirect('/success/')
  
  else: 
    form = SubscribeForm()

  return render(request, 'texting/index.html', {'form': form})
