from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Order
from .forms import AppointmentForm


#check name list code
#def index(request):
#    name_list = Order.objects.order_by('-name')[:2]
#    template = loader.get_template('scheduler/index.html')
#    context = {
#        'name_list': name_list,
#    }
#    return HttpResponse(template.render(context, request))

def index(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
        else:
            print "something is wrong"
    else:
        form = AppointmentForm()
    return render(request, 'scheduler/index.html', {'form': form})

def thanks(request):
    return HttpResponse("Thanks for making order! ")