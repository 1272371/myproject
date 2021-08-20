from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import ServiceOffered, ServiceTypes


# Create your views here.
def home(request):
    return render(request, 'home.html')


def services(request):
    services = ServiceOffered.objects.all()
    return render(request, 'services.html', {'services': services})


def services_offered(request, pk):
    service = get_object_or_404(ServiceOffered, pk=pk)
    return render(request, 'types.html', {'st': service})


def service_type(request, pk):
    serviceType = get_object_or_404(ServiceTypes, pk=pk)
    return render(request, 'servicestypes.html', {'st': serviceType})
