from django.shortcuts import render
from django.http import HttpResponse
from .models import Allocated
from .forms import FeedbackForm

# Create your views here.
def index(request):
    return render(request, 'helplines/index.html')

def bedDetails(request):
    beds = Allocated.objects.all()
    return render(request, 'helplines/bedDetails.html',{'beds':beds})

def remInjection(request):
    return render(request, 'helplines/remInjection.html')

def careCenter(request):
    return render(request, 'helplines/careCenter.html')

def freeVaccination(request):
    return render(request, 'helplines/freeVaccination.html')

def helplineDetail(request):
    return render(request, 'helplines/helplineDetail.html')

def o2Cylinders(request):
    return render(request, 'helplines/o2Cylinders.html')

def testingCenter(request):
    return render(request, 'helplines/testingCenter.html')

def feedback(request):
    print(request.GET)
    return render(request, 'helplines/index.html')

def disclaimer(request):
    return render(request, 'helplines/disclaimer.html')